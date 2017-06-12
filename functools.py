#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
maskedpy.functools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (c) 2017, MaskedW maskedw00@gmail.com
License: MIT (see LICENSE for details)
"""

import traceback


def overrides(interface_class):
    """
    オーバーライドしたつもりのタイポを防ぎます。
    http://stackoverflow.com/questions/1167617/in-python-how-do-i-indicate-im-overriding-a-method
    """
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider


def not_overrides(interface_class):
    """
    overrides()とは逆で、意図せずにオーバーライドしてしまうことを防ぎます。
    """
    def not_overrider(method):
        assert(method.__name__ not in dir(interface_class))
        return method
    return not_overrider


class FunctionUtil(object):
    @staticmethod
    def func_name():
        stack = traceback.extract_stack()
        filename, codeline, funcname, text = stack[-2]
        return funcname
