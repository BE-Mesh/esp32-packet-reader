#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Serial reader


"""
import serial
import logging

logger = logging.getLogger('reader')


class Reader:
    def __init__(self, path: str):
        self.path: str = path
        self.ser: serial.Serial = serial.Serial(
            baudrate=115200,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )

    def open_reader(self):
        logger.info('Starting serial connection')

        try:
            self.ser.port = self.path
            self.ser.open()
            return True
        except serial.serialutil.SerialException as err:
            raise err

    def get_data(self):
        data = self.ser.readline()
        logger.info(data.decode("utf-8"))
        logger.info(data)
        return data

    def close_reader(self):
        self.ser.close()
