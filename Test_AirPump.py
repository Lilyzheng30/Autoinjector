from machine import ADC, Pin #tell MicroPython that we want to use these libraries in our code
from time import sleep

ISEMeter = ADC(Pin(27))
MyRobot = Pin(14,Pin.OUT) #Configure GP15 as a digital output
MyRobot.value(0)

from machine import ADC, Pin #tell MicroPython that we want to use these libraries in our code
from time import sleep

ISEMeter = ADC(Pin(27))
MyRobot = Pin(14,Pin.OUT) #Configure GP15 as a digital output
MyRobot.value(1)
