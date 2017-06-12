#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
maskedpy.object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (c) 2017, MaskedW maskedw00@gmail.com
License: MIT (see LICENSE for details)
"""

class ObjectUtil(object):

    @staticmethod
    def class_name(obj):
        if hasattr(obj, '__name__'):
            return obj.__name__
        else:
            return type(obj).__name__
