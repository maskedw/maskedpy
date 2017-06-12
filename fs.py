#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
maskedpy.fs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (c) 2017, MaskedW maskedw00@gmail.com
License: MIT (see LICENSE for details)
"""

import os
import errno


class FileSystemUtil(object):
    @staticmethod
    def find_rootdir(rootkey='.git', max_depth=30):
        for i in range(max_depth):
            if os.path.exists(rootkey):
                return os.path.dirname(os.path.abspath(rootkey))
            rootkey = '../' + rootkey
        return None

    @staticmethod
    def makedirs(path):
        if not path:
            return
        path = str(path)

        """
        http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
        """
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise


class ScopedChDir(object):
    def __init__(self, path):
        self.old_dir = os.getcwd()
        self.new_dir = str(path)

    def __enter__(self):
        os.chdir(self.new_dir)

    def __exit__(self, *args):
        os.chdir(self.old_dir)
