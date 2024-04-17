from gpiozero import LED
from time import sleep

#Introduzco las variables de los led
ledred = LED(13)
ledblue = LED(19)
ledgreen = LED(26)
#Introduzco las variables de contadores
rojo = 0
azul = 0
verde = 0

#Inicio un bucle
while True:

#Determino en que numerons del contador "rojo" LED rojo estara prendido
	if rojo < 4:
		ledred.on()
	if rojo >=4:
		ledred.off()

#Determino en que numeros del contador "azul" el LED azul estara prendido
	if azul <2:
		ledblue.on()
	if azul >=2:
		ledblue.off()

#Determino en que numeros del contador "verde" el LED verde estara prendido
	if verde == 0:
		ledgreen.on()
	if verde == 1:
		ledgreen.off()

#Sumo 1 a cada contador
	rojo = rojo + 1
	azul = azul + 1
	verde = verde + 1

#Vuelvo a cero a los contadores que se pasaron de su limite
	if rojo == 8:
		rojo = 0
	if azul == 4:
		azul = 0
	if verde == 2:
		verde = 0
#Espero 250us. EL valor de esta pausa determina la frecuencia con la que corre el bucle
	sleep(0.25)


