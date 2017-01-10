#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Graphite Eagle Commands."""

import socket
import time
import xml.etree.ElementTree as ET

import graphiteeagle


__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'



class CarbonHost(object):

    """
    Object Class for a Carbon Host.
    """

    def __init__(self, host, port=None):
        self.address = (host, port or 2003)
        self.socket = socket.socket()

    def __del__(self):
        self.close()

    def connect(self):
        """Connects to the Carbon Host."""
        self.socket.connect(self.address)

    def close(self):
        """Closes the connection."""
        self.socket.close()

    def collect(self, name, value, timestamp):
        """Collects metrics to send to the Carbon Host."""
        self.socket.send("%s %d %d\n" % (name, value, timestamp))


class EagleHost(object):

    """
    Object Class for a Eagle Host.
    """

    def __init__(self, host, port=None):
        self.address = (host, port or graphiteeagle.EAGLE_PORT)
        self.socket = socket.socket()

    def __del__(self):
        self.close()

    def connect(self):
        """Connects to the Eagle Host."""
        self.socket.connect(self.address)

    def close(self):
        """Closes the connection."""
        self.socket.close()

    def get_current_demand(self, callback=None):
        """Gets the CURRENT demand from the Eagle Host."""
        xml_demand = self._query_eagle()
        current_demand = self._parse_demand(xml_demand)

        if callback:
            return callback(current_demand)
        else:
            return current_demand

    def _parse_demand(self, xml_demand):
        root = ET.fromstring(xml_demand)

        demand = root.findall('Demand')[0].text
        multiplier = root.findall('Multiplier')[0].text
        divisor = root.findall('Divisor')[0].text

        demand_f = float(int(demand, 16))
        multiplier_f = float(int(multiplier, 16))
        divisor_f = float(int(divisor, 16))

        current_demand = demand_f * multiplier_f / divisor_f
        return current_demand

    def _query_eagle(self):
        sock_buf = ''
        self.socket.send(graphiteeagle.COMMAND)
        while 1:
            buf = self.socket.recv(1000)
            if not buf:
                break
            sock_buf += buf
        return sock_buf
