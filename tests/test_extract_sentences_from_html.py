#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""File to test the function to extract sentences from html documents"""
# ---------------------------------------------
# System modules
# ---------------------------------------------
import sys
sys.path.append("..")
import logging
import unittest
from unittest import TestCase
# ---------------------------------------------
# External dependencies
# ---------------------------------------------
# ---------------------------------------------
# Local dependencies
# ---------------------------------------------
from preprocessing.extract_sentences_from_html import extract_sentences_from_html
# ---------------------------------------------


# ---------------------------------------------
# Config
# ---------------------------------------------
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)


# 1.* Test if a new line is introduced before <ul> and <li> tags.
# 2. Test if the invalid tags are being removed and their children text is kept.
# 3.* Test if the pesky tags are being deleted.
# 4. Test the handling of <br> tags
# 5. Test the removal of comments
# 6. Test the replacement of <p> and <li> tags with LINE_BREAK
# 7. Test the replacement of multiple consecutive whitespaces with LINE_BREAK
# 8. Test the replacement of email addresses with EMAIL_ADDRESS
# 9. Test the replacement of urls with URL_ADDRESS
# 10. Test the splitting of the text by the LINE_BREAK token
# 11. Test the sentence splitter tokenizer


class TestSentenceExtractor(TestCase):

    def test_hanlding_unordered_lists(self):
        #
        # Extract stuff right <li>
        #
        self.assertSequenceEqual(extract_sentences_from_html("""
            <html><body>
                Hallo du wie inkl. und weiter <br/>
                Hallo du wie incl. und weiter <br/>
                Hallo du wie u.v.m. und weiter <br/>
                Hallo du wie u.a. und weiter <br/>
                Hallo du wie u.n. und weiter <br/>
                Hallo du wie o.ä. und weiter <br/>
                Hallo du wie i.b. und weiter <br/>
                Hallo du wie jhrl. und weiter <br/>
                Hallo du wie e.v. und weiter <br/>
                Hallo du wie n.v. und weiter <br/>
                Hallo du wie mio. und weiter <br/>
                Hallo du wie tel.-nr. und weiter <br/>
                Hallo du wie telefon-nr. und weiter <br/>
                Hallo du wie nr. und weiter <br/>
                Hallo du wie max. und weiter <br/>
                Hallo du wie min. und weiter <br/>
                Hallo du wie abs. und weiter <br/>
                Hallo du wie o.g. und weiter <br/>
                Hallo du wie referenz-nr. und weiter <br/>
                Hallo du wie ref.-nr. und weiter <br/>
                Hallo du wie z.t. und weiter <br/>
                Hallo du wie mind. und weiter <br/>
                Hallo du wie insb. und weiter <br/>
                Hallo du wie bezgl. und weiter <br/>
                Hallo du wie zusätzl. und weiter <br/>
                Hallo du wie gem. und weiter <br/>
                Hallo du wie verggr. und weiter <br/>
                Hallo du wie stellv. und weiter <br/>
                Hallo du wie etc. und weiter <br/>
                Hallo du wie z.z. und weiter <br/>
                Hallo du wie tvöd. und weiter <br/>
                Hallo du wie s-bhf. und weiter <br/>
                Hallo du wie z.b. und weiter <br/>
                Hallo du wie dr. und weiter <br/>
                Hallo du wie a.m. und weiter <br/>
                Hallo du wie dr.med. und weiter <br/>
                Hallo du wie tel. und weiter <br/>
                Hallo du wie bzw. und weiter <br/>
                Hallo du wie bzgl. und weiter <br/>
                Hallo du wie ggf. und weiter <br/>
                Hallo du wie ggfs. und weiter <br/>
                Hallo du wie ca. und weiter <br/>
                Hallo du wie z. und weiter <br/>
                Hallo du wie hd. und weiter <br/>
                Hallo du wie dipl.ing. und weiter <br/>
                Hallo du wie dipl.-ing. und weiter <br/>
                Hallo du wie dipl.kfm. und weiter <br/>
                Hallo du wie dipl.-kfm. und weiter <br/>
                Hallo du wie dt. und weiter <br/>
                Hallo du wie co. und weiter <br/>
                Hallo du wie zzgl. und weiter <br/>
                Hallo du wie str. und weiter <br/>
                Hallo du wie gr. und weiter <br/>
                Hallo du wie d.h. und weiter <br/>
                Hallo du wie dgl. und weiter <br/>
                Hallo du wie d.i. und weiter <br/>
                Hallo du wie ehem. und weiter <br/>
                Hallo du wie amtl. und weiter <br/>
                Hallo du wie entspr. und weiter <br/>
                Hallo du wie evtl. und weiter <br/>
                Hallo du wie fa. und weiter <br/>
                Hallo du wie gegr. und weiter <br/>
                Hallo du wie hrn. und weiter <br/>
                
            <body></html>
        """).get('sentences'), [
            "Hallo du wie inkl. und weiter",
            "Hallo du wie incl. und weiter",
            "Hallo du wie u.v.m. und weiter",
            "Hallo du wie u.a. und weiter",
            "Hallo du wie u.n. und weiter",
            "Hallo du wie o.ä. und weiter",
            "Hallo du wie i.b. und weiter",
            "Hallo du wie jhrl. und weiter",
            "Hallo du wie e.v. und weiter",
            "Hallo du wie n.v. und weiter",
            "Hallo du wie mio. und weiter",
            "Hallo du wie tel.-nr. und weiter",
            "Hallo du wie telefon-nr. und weiter",
            "Hallo du wie nr. und weiter",
            "Hallo du wie max. und weiter",
            "Hallo du wie min. und weiter",
            "Hallo du wie abs. und weiter",
            "Hallo du wie o.g. und weiter",
            "Hallo du wie referenz-nr. und weiter",
            "Hallo du wie ref.-nr. und weiter",
            "Hallo du wie z.t. und weiter",
            "Hallo du wie mind. und weiter",
            "Hallo du wie insb. und weiter",
            "Hallo du wie bezgl. und weiter",
            "Hallo du wie zusätzl. und weiter",
            "Hallo du wie gem. und weiter",
            "Hallo du wie verggr. und weiter",
            "Hallo du wie stellv. und weiter",
            "Hallo du wie etc. und weiter",
            "Hallo du wie z.z. und weiter",
            "Hallo du wie tvöd. und weiter",
            "Hallo du wie s-bhf. und weiter",
            "Hallo du wie z.b. und weiter",
            "Hallo du wie dr. und weiter",
            "Hallo du wie a.m. und weiter",
            "Hallo du wie dr.med. und weiter",
            "Hallo du wie tel. und weiter",
            "Hallo du wie bzw. und weiter",
            "Hallo du wie bzgl. und weiter",
            "Hallo du wie ggf. und weiter",
            "Hallo du wie ggfs. und weiter",
            "Hallo du wie ca. und weiter",
            "Hallo du wie z. und weiter",
            "Hallo du wie hd. und weiter",
            "Hallo du wie dipl.ing. und weiter",
            "Hallo du wie dipl.-ing. und weiter",
            "Hallo du wie dipl.kfm. und weiter",
            "Hallo du wie dipl.-kfm. und weiter",
            "Hallo du wie dt. und weiter",
            "Hallo du wie co. und weiter",
            "Hallo du wie zzgl. und weiter",
            "Hallo du wie str. und weiter",
            "Hallo du wie gr. und weiter",
            "Hallo du wie d.h. und weiter",
            "Hallo du wie dgl. und weiter",
            "Hallo du wie d.i. und weiter",
            "Hallo du wie ehem. und weiter",
            "Hallo du wie amtl. und weiter",
            "Hallo du wie entspr. und weiter",
            "Hallo du wie evtl. und weiter",
            "Hallo du wie fa. und weiter",
            "Hallo du wie gegr. und weiter",
            "Hallo du wie hrn. und weiter"
        ])
        self.assertSequenceEqual(extract_sentences_from_html("""
            <html><body>
                Sentence 1
                <ul class="ul">
                    <li>Li 1</li>
                    <li>Li 2</li>
                    <li>Li 3</li>
                </ul>
            <body></html>
        """).get('sentences'), ["Sentence 1", 'Li 1', 'Li 2', 'Li 3'])
        #
        # Extract stuff right
        #
        self.assertSequenceEqual(extract_sentences_from_html("""
            <html><body>
                <p>
                    Sentence oder. Sentence and so on!
                </p>

                <ul class="ul">
                    <li>Li 1</li>
                    <li>Li 2</li>
                    <li>Li 3
                        <ul class="ul">
                            <li>Li A</li>
                            <li>Li B</li>
                            <li>Li C</li>
                        </ul>
        
                    </li>
                </ul>
            <body></html>
        """).get('sentences'), ["Sentence oder.", "Sentence and so on!", 'Li 1', 'Li 2', 'Li 3', 'Li A', 'Li B', 'Li C'])


    def test_newline_insertion(self):
        #
        # Make sure that the right sentences are extracted!
        #
        self.assertSequenceEqual(extract_sentences_from_html("""
            <html><body>
                Sentence 1
                <ul class="ul">Sentence 2</ul>
            <body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])
        #
        # Make sure that the right sentences are extracted!
        #
        self.assertSequenceEqual(extract_sentences_from_html("""
            <html>
                <body>
                    Sentence 1
                    <li class="li">Sentence 2</li>
                <body>
            </html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])

    def test_removal_of_invalid_tags(self):
        #
        # is this the right method name?
        #
        self.assertSequenceEqual(extract_sentences_from_html("""
            <html><body>
                <div> Sentence 3 </div>\n
                <div> Sentence 4 </div>
            <body></html>
        """).get('sentences'), ['Sentence 3', 'Sentence 4'])
        #
        # is this the right method name?
        #
        self.assertSequenceEqual(extract_sentences_from_html("""
            <html><body>
                <div> Sentence 5  </div>
                <div> Sentence 6 </div>
            <body></html>
        """).get('sentences'), ['Sentence 5', 'Sentence 6'])

    def test_removal_of_pesky_tags(self):

        # Removal of a <script> tag
        self.assertCountEqual(extract_sentences_from_html("""
            <html>
               <head>
                    <title> TITLE </title>
                      <meta content="some_person@stepstone.de" name="author">
                      <link href="https://www.stepstone.de/stellenangebote--Senior-Product-Owner-m-w--4905353-inline.html" rel="canonical">
                 </head>
                <body>
                    <style> css text </style>
                    <div> Sentence 1  </div>
                    <div> Sentence 2 </div>
                <body>
                    <form>
                        Das ist ein FORM
                        <input type="text"/>
                        <input type="text"/>
                    </form>  
                <div>
                    <svg width="100" height="100"><circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" /></svg>
                </div>  
                <pre>Preformatted Text</pre>
                <noscript>Your browser does not support JavaScript!</noscript>     
                <script> javascript code </script>
                  <button type="button">Click Me!</button>
              <img src="https://gebit.prescreenapp.io/uploads/company/job_banner/2515.jpg" class="img-responsive" alt="banner" >
              <iframe src="www.google.com">This is a iframe</iframe>
            </html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html>
                <body>
                    <h1>This is heading 1</h1>
                    <div>Sentence A</div>
                    <div>Sentence B</div>
                <body>
            </html>
        """).get('sentences'), ["This is heading 1", 'Sentence A', 'Sentence B'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <h2>This is heading 2</h2>
                <div> Sentence 1  </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ["This is heading 2", 'Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html>This is heading 3<body>
                <h3></h3>
                <div> Sentence 1  </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ["This is heading 3", 'Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <h4>This is heading 4</h4>
                <div> Sentence 1  </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ["This is heading 4", 'Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <h5>This is heading 5</h5>
                <div> Sentence 1  </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ["This is heading 5", 'Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <h6>This is heading 6</h6>
                <div> Sentence 1  </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ["This is heading 6", 'Sentence 1', 'Sentence 2'])
    #
    #
    # Handles <br> tags correctly!
    #
    def test_handling_of_br_tags(self):

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div> <br> Senior HR Manager </br> Sentence 1  </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ['Senior HR Manager', 'Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <br> Senior HR Manager </br>
                <div> Sentence 1  </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ['Senior HR Manager', 'Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div> 
                    <br/> 
                    Senior HR Manager </br> 
                    Sentence 1  
                </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ['Senior HR Manager', 'Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                The best </br>
                <br /> 
                Senior HR Manager </br>
                <div> Sentence 1  </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ["The best", 'Senior HR Manager', 'Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div>
                    <br> Senior HR Manager 
                    </ br> 
                    Sentence 1  
                </div>
                <div> 
                Sentence 2 </div>
            <body></html>
        """).get('sentences'), ['Senior HR Manager', 'Sentence 1', 'Sentence 2'])
    # ---------------------------------------------------------------------------
    #
    #
    #
    # ---------------------------------------------------------------------------

    def test_removal_of_comments(self):

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <!-- Placeholder column -->
                <div> Sentence A  </div>
                <div> Sentence B </div>
                <div> Sentence C </div>
            <body></html>
        """).get('sentences'), ['Sentence A', 'Sentence B', 'Sentence C'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div> Sentence 1  </div>
                <!-- Placeholder column -->
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div> Sentence 1  
                    <!-- Placeholder column -->
                </div>
                <div> Sentence 2 </div>
            <body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])
    # ---------------------------------------------------------------------------
    #
    #
    #
    # ---------------------------------------------------------------------------

    def test_handling_of_p_and_li_tags(self):
        #
        # Make sure it extract sentences from different paragraphs
        #
        self.assertSequenceEqual(extract_sentences_from_html("""
            <html><body>
                <div>
                    <p> Sentence A  </p>
                    <p> Sentence B </p>
                </div>
            <body></html>
        """).get('sentences'), ['Sentence A', 'Sentence B'])
        #
        # Make sure it extract sentences from different li
        #
        self.assertSequenceEqual(extract_sentences_from_html("""
            <html><body>
                <div>
                    <li> Sentence C </li>
                    <li> Sentence D </li>
                </div>
            <body></html>        
        """).get('sentences'), ['Sentence C', 'Sentence D'])
    # ---------------------------------------------------------------------------
    #
    #
    #
    # ---------------------------------------------------------------------------

    def test_handling_of_multiple_whitespaces(self):
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body><p> Sentence 1   Sentence 2 </p></div><body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body><p> Sentence 1    Sentence 2 </p></div><body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])
    # ---------------------------------------------------------------------------
    #
    #
    #
    # ---------------------------------------------------------------------------
    def test_replacing_cities(self):
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div>Hamburg 1   </div>\n
            <body></html>
        """).get('sentences'), ['CITY_STR 1'])

        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div>In Düsseldorf und am Rhein   </div>\n
            <body></html>
        """).get('sentences'), ['In CITY_STR und am Rhein'])


        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div>In Düsseldorf und Köln   </div>\n
            <body></html>
        """).get('sentences'), ['In CITY_STR und CITY_STR'])
        


    def test_handling_of_email_addresses(self):
        #
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div>Sentence 1   </div>\n<div>Sentence 2 user@company.de </div>
            <body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2 EMAIL_ADDRESS'])
        #
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div>C++    </div><div>Sentence 2 user+name@company-name.com </div>
            <body></html>
        """).get('sentences'), ['C++', 'Sentence 2 EMAIL_ADDRESS'])
        #
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div>Sentence 1   </div>\n<div>Sentence 2 user.name@companyname.com </div>
            <body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2 EMAIL_ADDRESS'])
    # ---------------------------------------------------------------------------
    #
    #
    #
    # ---------------------------------------------------------------------------

    def test_handling_of_urls(self):
        # Full URL
        self.assertCountEqual(extract_sentences_from_html("""
            <html>
                <body>
                    <div>Sentence 1   </div>\n
                    <div>Sentence 2 https://www.example.com </div>
                <body>
            </html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2 URL_ADDRESS'])
        # # Full image url
        self.assertCountEqual(extract_sentences_from_html("""
            <html>
                <body>
                    <div>Sentence 1   </div>\n<div>Sentence 2 https://www.example.com/media/picture.png </div>
                <body>
            </html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2 URL_ADDRESS'])
        #
        self.assertCountEqual(extract_sentences_from_html("""
            <html>
                <body>
                    <div>Sentence 1   </div>\n
                    <div>Sentence 2 https://www.example.com/apply </div>
                <body>
            </html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2 URL_ADDRESS'])
        #
        self.assertCountEqual(extract_sentences_from_html("""
            <html>
                <body>
                    <div>Sentence 1   </div>\n
                    <div>Sentence 2 http://example.net </div>
                <body>
            </html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2 URL_ADDRESS'])
        #
        # Ending with a slash
        #
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div>Sentence 1   </div>\n<div>Sentence 2 http://very/long/url/adress/ </div>
            <body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2 URL_ADDRESS'])
        # #
        # Ending with a slash
        #
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                <div>Sentence 1   </div>\n
                <div>Sentence 2 www.example.com </div>
                <div>vincentz@3punktS.de www.3punktS.de</div>
                Herr Trawny www.prismaplan.de
                <div>www.zi-mannheim.de</div>
                <p>Firmenlogo, verlinkt auf www.karriere-bei-lidl.de</p>
            <body></html>
        """).get('sentences'), [
            'Sentence 1', 
            'Sentence 2 URL_ADDRESS', 
            "EMAIL_ADDRESS URL_ADDRESS", 
            "Herr Trawny URL_ADDRESS",
            "URL_ADDRESS",
            "Firmenlogo, verlinkt auf URL_ADDRESS"
        ])
    # ---------------------------------------------------------------------------
    #
    #
    #
    # ---------------------------------------------------------------------------

    def test_splitting_by_LINE_BREAK_token(self):
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                Sentence 1 LINE_BREAK Sentence 2<body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                Sentence 1 LINE_BREAK LINE_BREAK Sentence 2<body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                LINE_BREAK Sentence 1 LINE_BREAK Sentence 2<body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                Sentence 1 LINE_BREAK Sentence 2 LINE_BREAK LINE_BREAK<body></html>
        """).get('sentences'), ['Sentence 1', 'Sentence 2'])
    # ---------------------------------------------------------------------------
    #
    #
    #
    # ---------------------------------------------------------------------------

    def test_sentence_splitter(self):

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                 Sentence 1! A longer - second sentence. Third sentence. 
            </body></html>
        """).get('sentences'), ['Sentence 1!', 'A longer - second sentence.', 'Third sentence.'])

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                 Sentence 1! 2nd sentence with German abbreviations like: inkl. or z.b. for example. Third sentence. 
            </body></html>
        """).get('sentences'), ['Sentence 1!', '2nd sentence with German abbreviations like: inkl. or z.b. for example.', 'Third sentence.'])

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                 Sentence 1! 2nd sentence with German abbreviations like: o.ä. or u.v.m. for example. Third sentence. 
            </body></html>
        """).get('sentences'), [
            'Sentence 1!',
            '2nd sentence with German abbreviations like: o.ä. or u.v.m. for example.',
            'Third sentence.'
        ])

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                 Sentence 1! 2nd sentence with German abbreviations like: u.a. or s-bhf. for example. Third sentence. 
            </body></html>
        """).get('sentences'), [
            'Sentence 1!',
            '2nd sentence with German abbreviations like: u.a. or s-bhf. for example.',
            'Third sentence.'
        ])

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                 Sentence 1! 2nd sentence with German abbreviations like: dr. or dr.med. for example. Third sentence. 
            </body></html>
        """).get('sentences'), [
            'Sentence 1!',
            '2nd sentence with German abbreviations like: dr. or dr.med. for example.',
            'Third sentence.'
        ])

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                 Sentence 1! 2nd sentence with German abbreviations like: tel. or bzw. for example. Third sentence. 
            </body></html>
        """).get('sentences'), [
            'Sentence 1!',
            '2nd sentence with German abbreviations like: tel. or bzw. for example.',
            'Third sentence.'
        ])

        # Should not split ggf. or ca.
        self.assertCountEqual(extract_sentences_from_html("""
            <html>
                <body>
                     Sentence 1! 2nd sentence with German abbreviations like: ggf. or ca. for example. Third sentence. 
                </body>
            </html>
        """).get('sentences'), [
            'Sentence 1!',
            '2nd sentence with German abbreviations like: ggf. or ca. for example.',
            'Third sentence.'
        ])

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html>
                <body>
                     Sentence 1! 2nd sentence with German abbreviations like: z. hd. or dipl.ing. for example. Third sentence. 
                </body>
            </html>
        """).get('sentences'), ['Sentence 1!', '2nd sentence with German abbreviations like: z. hd. or dipl.ing. for example.', 'Third sentence.'])

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                 Sentence 1! 2nd sentence with German abbreviations like: zzgl. for example. Third sentence. 
            </body></html>
        """).get('sentences'), ['Sentence 1!', '2nd sentence with German abbreviations like: zzgl. for example.', 'Third sentence.'])

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                 Sentence 1! 2nd sentence with German abbreviations like: str. or gr. for example. Third sentence. 
            </body></html>
        """).get('sentences'), ['Sentence 1!', '2nd sentence with German abbreviations like: str. or gr. for example.', 'Third sentence.'])

        # Some explainer
        self.assertCountEqual(extract_sentences_from_html("""
            <html><body>
                 Sentence 1! 2nd sentence with German abbreviations like: co. KG for example. Third sentence. 
            </body></html>
        """).get('sentences'), ['Sentence 1!', '2nd sentence with German abbreviations like: co. KG for example.', 'Third sentence.'])


if __name__ == '__main__':
    unittest.main()
