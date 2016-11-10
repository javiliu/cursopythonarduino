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
datoEnviar = input("Ingrese un numero:")

# Leer datos Arduino
while(True):
    if((len(datoEnviar) > 0) or (datoEnviar != "s") or (datoEnviar != "n")):
        # Envia datos a Arduino
        contador = int(datoEnviar)
        arduino.write(datoEnviar.encode())
        print("Enviando informacion, espere")        
        time.sleep(contador + 1)
        datoEnviar = input("Ingrese un numero:")

arduino.close()
