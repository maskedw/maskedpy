#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
maskedpy.platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (c) 2017, MaskedW maskedw00@gmail.com
License: MIT (see LICENSE for details)
"""

import platform
import os


class PlatformUtil(object):

    @staticmethod
    def is_windows():
        return platform.system().lower().find('windows') != -1

    @staticmethod
    def is_posix():
        return os.name.lower().find('posix') != -1
