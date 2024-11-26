from gpiozero import LED
from time import sleep

PinLed=LED(25)

while True:
	PinLed.on()
	print("LED aceso")
	sleep(1)
	PinLed.off()
	print("LED apagado")
	sleep(1)
