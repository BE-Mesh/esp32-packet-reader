#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Packet BLE Mesh based representation that has to be read by IDS


"""
import logging

logger = logging.getLogger('packet')


class Packet:
    def __init__(self):
        self.test = 'test'

    def __repr__(self):
        return f'Packet({self.test})'

    def __str__(self):
        return f'test: {self.test}'
