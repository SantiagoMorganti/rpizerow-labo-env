from gpiozero import LED
from time import sleep

ledred = LED(13)
ledblue = LED(19)
ledgreen = LED(26)
rojo = 0
azul = 0
verde = 0

while True:

	if rojo < 4:
		ledred.on()
	if rojo >=4:
		ledred.off()

	if azul <2:
		ledblue.on()
	if azul >=2:
		ledblue.off()

	if verde == 0:
		ledgreen.on()
	if verde == 1:
		ledgreen.off()

	rojo = rojo + 1
	azul = azul + 1
	verde = verde + 1

	if rojo == 8:
		rojo = 0
	if azul == 4:
		azul = 0
	if verde == 2:
		verde = 0

	sleep(0.25)


