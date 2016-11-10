# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Javier Adrian Liu Manzanilla, j4v13rlm
# Enviar datos Python3 a Arduino
"""
luisllamas.es
/2016/01/controlar-arduino-con-python-y-la-libreria-pyserial/
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
datoEnviar = input("Ingrese un dato:")

# Leer datos Arduino
while(True):
    if((len(datoEnviar) > 0) or (datoEnviar != "s") or (datoEnviar != "n")):
        # Envia datos a Arduino
        arduino.write(datoEnviar.encode())
        print("Recibiendo informacion, espere...")
        datoRecibido = arduino.read(arduino.inWaiting())
        print(datoRecibido.decode('ascii', errors='replace'), end='')
        time.sleep(2)

arduino.close()
