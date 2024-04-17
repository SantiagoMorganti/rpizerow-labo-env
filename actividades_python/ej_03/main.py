from gpiozero import LED, Buzzer
import time

# Inicialización de los componentes
red = LED(19)
green = LED(13)
blue = LED(26)
buzzer = Buzzer(22)


# Inicio un bucle 
while True:
#Solicito al usuario que ingrese al comando  y muestro el mensaje "prompt"
	comando = input("prompt: ").split()
#Me fijo que la longitud de la lista "comando" sea igual a 2
	if len(comando) == 2:
		accion, opcion = comando
#Prendo o apago el buzzer segun la opcion introducida
		if accion == "buzz":
			if opcion == "on":
				buzzer.on()
			elif opcion == "off":
				buzzer.off()
#Aviso si la opcion dada no es valida
			else:
				print("Comando inválido para el buzzer")
#Enciendo el rgb de solo el color indicado segun la opcion introducida
		elif accion == "rgb":
			if opcion == "red":
				red.on()
				blue.off()
				green.off()
			elif opcion == "green":
				green.on()
				red.off()
				blue.off()
			elif opcion == "blue":
				blue.on()
				red.off()
				green.off()
#Aviso si la opcion dada no es valida
			else:
				print("Comando inválido para el RGB")
#Aviso si el comando dado no es valido
		else:
			print("Comando no reconocido")
#Aviso si el  formato no fue respetado e indico el formato correcto
	else:
		print("Formato incorrecto. Debe ser [COMANDO] [OPCION]")
#Compruebo si el script se esta ejecutando como el programa principal
if __name__ == "__main__":
#Inicio un bloque de código donde se manejarán las excepciones
	try:
#Llamo la funcion "main()"
		main()
#Capturo la excepción "KeyboardInterrupt"
	except KeyboardInterrupt:
		rgb_off()
		buzzer_off()
