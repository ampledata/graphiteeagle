#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Graphite Eagle

"""
Graphite Eagle
~~~~
:author: Greg Albrecht <oss@undef.net>
:copyright: Copyright 2017 Greg Albrecht
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/graphiteeagle>
"""

from .constants import COMMAND, EAGLE_PORT  # NOQA
from .functions import get_instantaneous_demand  # NOQA
from .classes import CarbonHost, EagleHost  # NOQA

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'
