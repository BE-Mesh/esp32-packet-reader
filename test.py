#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Esp32 Packet reader

# TODO description

pip3 install -r ./requirements.txt
python3 test.py

"""
__author__ = "Andrea Lacava"
__credits__ = ["Andrea Lacava"]
__license__ = "GPL"
__version__ = "1.1"
__email__ = "thecave003@gmail.com"
__status__ = "Production"

import argparse
import logging

import serial

from reader.reader import Reader

DEFAULT_PATH = '/dev/ttyUSB0'


def test():
    path = DEFAULT_PATH
    logging.basicConfig(filename='run.log', filemode='w', level=logging.DEBUG)
    logger = logging.getLogger('packet_extractor')

    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', help='increase output verbosity',
                        action='store_true')

    parser.add_argument('-p', '--port', help='port on which esp is running')

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug('Verbose mode activated')

    if args.port:
        path = args.port

    reader = Reader(path=path)
    reader.open_reader()

    logger.info("Starting read")
    with open("trace.txt", 'w') as tracer:
        while 1:
            try:
                data = reader.get_data()
                print(data.decode("utf-8"))
                tracer.write(data.decode("utf-8"))
            except KeyboardInterrupt:
                logging.error("Keyboard quit")
                break

            except IndexError:
                tracer.flush()
                logging.error("Logger error")
                pass

            except serial.serialutil.SerialException as err:
                tracer.flush()
                logger.error("Serial exception")
                logger.error(err)
                pass

    reader.close_reader()
    logging.info('Closing read')


if __name__ == '__main__':
    test()
