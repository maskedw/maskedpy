#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
maskedpy.app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (c) 2017, MaskedW maskedw00@gmail.com
License: MIT (see LICENSE for details)
"""

import pathlib
import os
import __main__


class AppUtil(object):

    @staticmethod
    def app_name():
        """
        http://stackoverflow.com/questions/16474700/how-to-get-the-name-of-the-top-most-entry-script-in-python
        """

        fname = os.path.basename(__main__.__file__)
        ret = pathlib.Path(fname).stem
        return ret

    @staticmethod
    def app_dir():
        return os.path.dirname(__main__.__file__)
