#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
maskedpy.enum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (c) 2017, MaskedW maskedw00@gmail.com
License: MIT (see LICENSE for details)
"""

from enum import Enum


class AutoNumberEnum(Enum):
    """
    http://docs.python.jp/3/library/enum.html
    8.13.13.1. AutoNumber
    """
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class OrderedEnum(Enum):
    """
    http://docs.python.jp/3/library/enum.html
    8.13.13.2. OrderedEnum
    """
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class DuplicateFreeEnum(Enum):
    """
    http://docs.python.jp/3/library/enum.html
    8.13.13.3. AutoNumber
    """
    def __init__(self, *args):
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name
            raise ValueError(
                "aliases not allowed in DuplicateFreeEnum:  %r --> %r"
                % (a, e))
