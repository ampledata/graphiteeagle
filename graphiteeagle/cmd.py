#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Graphite Eagle Commands."""

import argparse

import graphiteeagle

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


def cli():
    """Command Line interface for Graphite Eagle."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--host', help='Carbon Host', default='localhost'
    )
    parser.add_argument(
        '-p', '--port', help='Carbon Port', default=2003
    )
    parser.add_argument(
        '-e', '--eagle', help='Eagle Host'
    )

    opts = parser.parse_args()

    carbon_host = graphiteeagle.CarbonHost(opts.host, opts.port)
    carbon_host.connect()

    eagle_host = graphiteeagle.EagleHost(opts.eagle)
    eagle_host.connect()

    eagle_host.get_current_demand(carbon_host.collect)


if __name__ == '__main__':
    cli()
