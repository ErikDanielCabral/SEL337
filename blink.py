from gpiozero import LED 	# Importa a classe LED da biblioteca gpiozero, que facilita o controle de GPIOs na Raspberry Pi.
from time import sleep 		# Importa a função sleep, usada para criar pausas entre as ações.

PinLed=LED(25)			# Cria um objeto LED associado ao pino GPIO 25 da Raspberry Pi. Este pino deve estar conectado ao LED.

while True:			# Inicia um loop infinito que será executado continuamente.
	PinLed.on()		# Liga o LED, enviando um sinal HIGH (3,3V) ao pino GPIO 25.
	print("LED aceso")	# Imprime no terminal que o LED está aceso.
	sleep(1)		# Aguarda por 1 segundo antes de continuar.
	PinLed.off()		# Desliga o LED, enviando um sinal LOW (0V) ao pino GPIO 25.
	print("LED apagado")	# Imprime no terminal que o LED está apagado.
	sleep(1)		# Aguarda por 1 segundo antes de reiniciar o loop.
