#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module extends the dictionary data structure"""


class AttrDict(dict):
    """Attribute-based wrapper for dictionaries.

    This class wraps a standard dictionary and adds
    capabilities to use it with an attribute-based approach.
    It also adds the tools to replace and override some keys based on
    another object exposing a dictionary interface (recursively).

    You can instatiate use it a normal dict, but also like an object:

    >>> obj = AttrDict(key='value')
    >>> obj['key']
    'value'
    >>> obj.key
    'value'
    >>> obj.key = 'something else'
    >>> obj.key
    'something else'

    If an attribute is a `dict`, it wil get converted to an `AttrDict` recursively,
    so this works:

    >>> obj = AttrDict()
    >>> obj.something = {}
    >>> obj.something.key = 'value'

    And also this:

    >>> obj = AttrDict(something=dict(key='value'))
    >>> obj.something.key
    'value'

    NOTE: When setting attributes, if the attribute is either `list`
    or `dict` it will get converted (recursively). Hence, the actual
    attribute stored inside `AttrDict` is not the same one. For that reason,
    the following code won't work:

    >>> obj = AttrDict()
    >>> my_list = []
    >>> obj.my_list = my_list
    >>> my_list.append(0)
    >>> obj.my_list
    []

    To make this code work, there order must be changed:

    >>> obj = AttrDict()
    >>> obj.my_list = []
    >>> my_list = obj.my_list
    >>> my_list.append(0)
    >>> obj.my_list
    [0]

    In conlusion, first assign and then take a reference of the assigned object, not
    the other way around. This behavior might change (transparently) in future implementations but
    it will always be safe to do it this way.
    """

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __setattr__(self, name, val):
        self[name] = self._convert(val)

    def __getattr__(self, name):
        try:
            attr = self[name]
        except KeyError:
            raise AttributeError(name)

        return attr

    def _convert(self, item):
        if isinstance(item, dict):
            return AttrDict(**item)
        if isinstance(item, list):
            return [self._convert(t) for t in item]
        return item

    def clone(self):
        """Returns a completely new instance deep cloned.

        >>> a = AttrDict(x=1, y=AttrDict(z=2))
        >>> b = a.clone()
        >>> id(a) == id(b)
        False
        >>> id(a.y) == id(b.y)
        False
        >>> b.x, b.y.z
        (1, 2)
        """
        return AttrDict._clone(self)

    @staticmethod
    def _clone(obj):
        if isinstance(obj, AttrDict):
            return AttrDict(**{k: AttrDict._clone(v) for k, v in obj.items()})
        if isinstance(obj, list):
            return [AttrDict._clone(x) for x in obj]
        else:
            return obj

    def merge(self, **other):
        """Take all the keys defined in `other` and override
        the corresponding keys (recursively) in this instance,
        returning a new instance.

        >>> a = AttrDict(x=1, y=AttrDict(z=3), w=0)
        >>> c = a.merge(x=3, z=4, y=AttrDict(z=5))

        `c` has all the new values plus the old ones that didn't change.
        >>> c.x
        3
        >>> c.y.z
        5
        >>> c.z
        4
        >>> c.w
        0

        `a` hasn't changed at all
        >>> a.x
        1
        >>> a.y.z
        3
        >>> 'z' in a
        False
        """

        return AttrDict._merge_parameters(self, other)

    @staticmethod
    def _merge_parameters(base, new):
        result = base.clone()

        for key, value in new.items():
            if isinstance(value, (dict, AttrDict)):
                base_value = base.get(key, AttrDict())
                result[key] = AttrDict._merge_parameters(base_value, value)
            else:
                result[key] = value

        return result
