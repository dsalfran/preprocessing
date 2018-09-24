#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf8
# ---------------------------------------------
# System modules
# ---------------------------------------------
import re
import logging
# ---------------------------------------------
# External dependencies
# ---------------------------------------------
from bs4 import BeautifulSoup, Comment
from langdetect import detect
# ---------------------------------------------
# Local dependencies
# ---------------------------------------------
from config import cities_list
from preprocess__sentences_splitter import sentence_splitter
from utils import fix_encoding_of_string
from config import html_parser
# ---------------------------------------------


# ---------------------------------------------
# Config
# ---------------------------------------------
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


with open(cities_list) as f:
    cities = f.read().lower().splitlines()


pesky_tags = ['script', 'style', 'form', 'link', 'img', 'iframe', 'head',
              'noscript', 'svg', 'meta', 'button', 'pre']

# 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
# The lists of tags, which should be removed, but where the inner content
# should stay. Mostly inline elements.
invalid_tags = ['b', 'i', 'u', 'a', 'font', 'strong', 'center',
                'span']
# Regex to capture url addresses
WEB_URL_REGEX = r"(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))(?=$|.)"


# Takes in a HTML string and returns a dict of sections
def extract_sentences_from_html(html_string, detect_german=False, pesky_tags=pesky_tags, parser_type=html_parser):
    logger.debug("called")
    """
        Turn a given HTML string into a array of sentences

        Example:
            html_string:
                    => "<html><body>Hallo World! Das ist cool.</body></html>"
            output:
                    => ["Hello world!", "Das ist cool"]
    """

    # Patch to avoid this: SozialesKrankenhäuserMedizinische
    html_string = re.sub(r'<ul ', r'\n\n\n<ul ', html_string)
    html_string = re.sub(r'<li ', r'\n\n\n<li ', html_string)
    logger.debug("Html string {}".format(html_string))

    # Needs to be wrapped in a try-catch because HTML can easily throw of
    # things.
    try:
        # Turns the HTML into a pyhton data structure

        # Clearning: Removes all variations of the <br> (forced line break) tag
        # --------------
        # This is a big decision, since we merge some blocks together that
        # aren't suppose to belog togehter. The upside is that we get
        # better sentences in the long run, because we avoid issues where
        # people use <br> for layout purposes is not
        #
        html_string = html_string.replace("<br>", " LINE_BREAK ")
        html_string = html_string.replace("<br/>", " LINE_BREAK ")
        html_string = html_string.replace("<br />", " LINE_BREAK ")
        html_string = html_string.replace("</br>", " LINE_BREAK ")
        html_string = html_string.replace("</ br>", " LINE_BREAK ")
        # Remove all new lines (\n) because authors
        html_string = html_string.replace("\n", " ")
        logger.debug("Text {}".format(html_string))

        soup = BeautifulSoup(html_string, parser_type)
        logger.info("Parsed text {}".format(soup.text))

        # Start removing the tags in each node of the HTML document
        for tag in invalid_tags:
            for match in soup.findAll(tag):
                # This methods removes a tag and keeps the inner text
                # Example:  <span>Hello</span> ==> Hello
                match.replaceWithChildren()

        logger.debug("Clearning: Removes the surounding tags of a give DOM, but keep the text")

        # Remove all the non relevant HTML tags
        for tag in pesky_tags:
            for node in soup.find_all(tag):
                node.decompose()

        # Remove comments
        comments = soup.findAll(text=lambda text: isinstance(text, Comment))
        [comment.extract() for comment in comments]

        # The token `LINE_BREAK` is our way to later split by this char.
        text = str(soup)

        text = re.sub(r"</p>", "</p> LINE_BREAK ", text)
        text = re.sub(r"</li>", "</li> LINE_BREAK ", text)
        text = re.sub(r"</h1>", "</h1> LINE_BREAK ", text)
        text = re.sub(r"</h1>", "</h1> LINE_BREAK ", text)
        text = re.sub(r"</h2>", "</h1> LINE_BREAK ", text)
        text = re.sub(r"</h3>", "</h1> LINE_BREAK ", text)
        text = re.sub(r"</h4>", "</h1> LINE_BREAK ", text)
        text = re.sub(r"</h5>", "</h1> LINE_BREAK ", text)
        text = re.sub(r"</h6>", "</h1> LINE_BREAK ", text)
        text = re.sub(r"</div>", "</div> LINE_BREAK ", text)

        logger.info("-----------> text (0) " + text)

        text = BeautifulSoup(text, parser_type).text

        logger.info("-----------> text (1) " + text)

        # logger.info("Text {}".format(text))

        # Remove all occurances where there are more than 3 consecutive whitespaces
        # Replace the pattern with our LINE_BREAK token, that we later use
        # To split these sections.
        pattern = r'(\s)\1{3,}'
        repl = r' LINE_BREAK '
        text = re.sub(pattern, repl, text, flags=re.DOTALL)

        # After the run before, now do the same with two consecutive whitespaces
        pattern = r'(\s)\1{2,}'
        repl = r' LINE_BREAK '
        text = re.sub(pattern, repl, text, flags=re.DOTALL)

        # Replace all emails with a token
        pattern = r'[\w\.-\\+]+@[\w\.-]+'
        repl = r'EMAIL_ADDRESS'
        text = re.sub(pattern, repl, text, flags=re.DOTALL)

        # TODO: Either modify the regex to capture urls or handle ambigous
        # abbrevations before searching urls in the text.
        text = re.sub(r'(co.kg)|(co.KG)', 'co. KG', text)

        # Replace all urls with a token

        logger.info("-----------> text (2.a) ")

        text = fix_encoding_of_string(text)

        def replaceUrls(some_str):
            return re.sub(WEB_URL_REGEX, "URL_ADDRESS", some_str, 0, re.DOTALL)

        def replaceCities(some_str):
            if(some_str == ""):
                return some_str

            # TODO: Optimize regex replacement
            cities_regex = re.compile("|".join(cities))

            for city in cities:
                some_str = re.sub(r'(^|\s)' + re.escape(city) + '( |$)', r'\1CITY_STR\2', some_str, flags=re.IGNORECASE)
            return some_str

        logger.debug("Replaced all special characters in the sentences")

        text = replaceCities(text)

        arr = text.split("LINE_BREAK")

        arr = list(map(str.strip, arr))

        arr = [replaceUrls(x) for x in arr]
        # arr = [ for word in arr]

        # Remove empty entries
        arr = list(filter(None, arr))
        # arr = list(filter("", arr))
        # Strip each string

        logger.info("-----------> text (2) " + str(arr))

        all_sentences = []

        for item in arr:
            # Turn the item in the array into a tokinized structure
            arrr = sentence_splitter.tokenize(item)
            for s in arrr:

                if detect_german:
                    #
                    # Let's throw out non-german sentences
                    #
                    try:
                        lang = detect(s)
                        if(lang == "de"):
                            logger.debug("✅  %s", s)
                            all_sentences.append(s)
                        else:
                            logger.debug("The sentence is not german. Lang: %s Sentence %s", lang, s)
                    except Exception as e:
                        logger.error("Error %s", str(e))
                else:
                    # s = re.sub(r'\.$', '', s)
                    all_sentences.append(s)

        logger.debug("Returning with %s", all_sentences)
        return {"sentences": all_sentences}
    except Exception as e:
        logger.error("Error %s", str(e))
        return {}
