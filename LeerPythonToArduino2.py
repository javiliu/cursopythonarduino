#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Lectura de datos desde un Arduino
#
# Basado en el ejemplo AnalogInOutSerial de Arduino (CC-BY-SA 3.0)
# http://arduino.cc/en/Tutorial/AnalogInOutSerial

import time

try:
    import serial
    # arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1.0)
    arduino = serial.Serial('COM3', baudrate = 9600, timeout = 1.0)

    # Nota: provocamos un reseteo manual de la placa para leer desde
    # el principio, ver http://stackoverflow.com/a/21082531/554319
    arduino.setDTR(False)
    time.sleep(1)
    arduino.flushInput()
    arduino.setDTR(True)

except (ImportError, serial.SerialException):
    # No hay módulo serial o placa Arduino disponibles
    import io

    class FakeArduino(io.RawIOBase):
        """Clase para representar un "falso Arduino"
        """
        def readline(self):
            time.sleep(0.1)
            return b'sensor = 0\toutput = 0\r\n'

    arduino = FakeArduino()


# Con la sentencia with el arduino se cierra automáticamente, ver
# http://docs.python.org/3/reference/datamodel.html#context-managers
with arduino:
    while True:
        try:
            # En Python 3 esta función devuelve un objeto bytes, ver
            # http://docs.python.org/3/library/stdtypes.html#typebytes
            dato = arduino.readline()
            # Con errors='replace' se evitan problemas con bytes erróneos, ver
            # http://docs.python.org/3/library/stdtypes.html#bytes.decode
            # Con end='' se evita un doble salto de línea
            print(dato.decode('ascii', errors='replace'), end='')

        except KeyboardInterrupt:
            print("Exiting")
            break
