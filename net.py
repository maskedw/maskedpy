#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
maskedpy.net
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (c) 2017, MaskedW maskedw00@gmail.com
License: MIT (see LICENSE for details)
"""

import socket
import netifaces


class NetUtil(object):
    @staticmethod
    def sock_is_open(host, port):
        """
        http://stackoverflow.com/questions/7436801/identifying-listening-ports-using-python
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        r = s.connect_ex((host, port))
        s.close()
        return r == 0

    @staticmethod
    def ip_address(ifname):
        """
        http://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python
        """
        ip = netifaces.ifaddresses(ifname)[2][0]['addr']
        return ip

    @staticmethod
    def mac_address(ifname):
        """
        https://stackoverflow.com/questions/159137/getting-mac-address
        """
        mac = netifaces.ifaddresses(ifname)[netifaces.AF_LINK]
        return mac['addr']
