# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Javier Adrian Liu Manzanilla, j4v13rlm
# Leer datos enviados por Arduino, Python3
"""
http://pybonacci.org/2014/01/19/leer-datos-de-arduino-desde-python/
"""
import serial
import time

arduino = serial.Serial('COM3', 9600, timeout = 0)
# Reset manual del Arduino
arduino.setDTR(False)
time.sleep(2)
# Reiniciar manualmente la placa arduino
arduino.flushInput()
arduino.setDTR(True)
# print(rawString)
# print ('\nValor retornado de Arduino: %s' % (rawString))
# rawString = rawString.rstrip('\n')

# Leer datos Arduino
while(True):
    datoLeer = arduino.readline()
    print(datoLeer.decode('ascii', errors='replace'), end='')

arduino.close()
