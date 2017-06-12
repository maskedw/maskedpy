#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
maskedpy.itertools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (c) 2017, MaskedW maskedw00@gmail.com
License: MIT (see LICENSE for details)
"""

import collections


def unique(iterable):
    """
    http://stackoverflow.com/questions/12878833/python-unique-list-using-set
    """
    keys = collections.OrderedDict.fromkeys(iterable).keys()
    return [k for k in keys]


def first_of(iterable):
    """
    iterableのはじめの要素を返します。
    """
    for x in iterable:
        return x


def find_first_of(predicate, iterable):
    """
    iterableからpredicateがTrueを返すはじめの要素を返します。
    """
    for x in iterable:
        if predicate(x):
            return x
    return None


def flatten(nested_list):
    """
    http://d.hatena.ne.jp/xef/20121027/p2
    x = flatten([[1,2],[3,4,[5,6]]])
    result x => [1, 2, 3, 4, 5, 6]
    """
    result = []
    for element in nested_list:
        if (isinstance(element, collections.Iterable) and
                not isinstance(element, str)):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result


def chunks(l, n):
    """
    http://d.hatena.ne.jp/yuheiomori0718/20140405/1396674065
    digits = [1,2,3,4,5]
    print(list(chunks(digits, 3)))
    [[1,2,3], [4,5]]
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]
