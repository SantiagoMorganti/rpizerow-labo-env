#importo las funciones LED y Button de la libreria gpiozero
from gpiozero import LED, Button
#importo la funcion pause de la libreria signal
from signal import pause

#introduzco las variables que corresponden a los perifericos del micro
led = LED(17)
button = Button(3)

#creo dos bulcles
#mientras que el boton sea presionado el led estara encendido
#mientras que el boton no este siendo presionado el boton estara apagado
button.when_pressed = led.on
button.when_released = led.off

pause()
