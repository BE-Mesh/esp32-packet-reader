#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Esp32 Packet reader

# TODO description

pip3 install -r ./requirements.txt
python3 main.py

"""
import sys  # ctrl-c handling and clear handling
import serial
import os
import logging
import argparse

DEFAULT_PATH = '/dev/ttyUSB0'

if __name__ == '__main__':
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

    logger.info('Starting serial connection')

    try:
        ser = serial.Serial(
            port=path,
            baudrate=115200,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )
    except serial.serialutil.SerialException as err:
        logger.error("Serial exception, coming out")
        logger.error(err)
        sys.exit(-1)

    with open("trace.txt", 'w') as tracer:
        while 1:
            try:
                data = ser.readline()
                print(data.decode("utf-8"))
                logger.info(data.decode("utf-8"))

            except KeyboardInterrupt:
                tracer.flush()
                tracer.close()
                ser.close()
                logging.error("Keyboard ")
                sys.exit()

            except IndexError:
                tracer.flush()
                logging.error("Logger error")
                pass

            except serial.serialutil.SerialException as err:
                tracer.flush()
                logger.error("Serial exception")
                logger.error(err)
                pass
