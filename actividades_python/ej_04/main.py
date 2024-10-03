from gpiozero import PWMLED
import ADS1x15
import time
import math

# Inicialización del ADC (ADS1115) con dirección I2C y modo de operación
adc = ADS1x15.ADS1115(1, 0x48)
adc.setMode(adc.MODE_SINGLE)
adc.setGain(adc.PGA_4_096V)

# Factor de conversión para pasar de lectura a voltaje
conversion_factor = adc.toVoltage()

# Configuración de los LEDs PWM para controlar el brillo
led_azul = PWMLED(26)
led_rojo = PWMLED(19)

# Parámetros para el cálculo de temperatura con el termistor
vcc_ref = 3.3
resistencia_fija = 10000
beta_termistor = 3900
temp_referencia = 298.15  # En Kelvin (25°C)
temp_actual = 0  # Temperatura calculada en °C
resistencia_termistor = 0

# Bucle principal
while True:
    # Lectura de los canales del ADC
    valor_potenciometro = adc.readADC(3)
    valor_termistor = adc.readADC(1)

    # Conversión a voltaje
    voltaje_potenciometro = valor_potenciometro * conversion_factor
    voltaje_termistor = valor_termistor * conversion_factor

    # Cálculo de la resistencia del termistor a partir de la lectura
    resistencia_termistor = (resistencia_fija * voltaje_termistor) / (vcc_ref - voltaje_termistor)

    # Cálculo de la temperatura con la ecuación de Steinhart-Hart
    temp_actual = beta_termistor / (math.log(resistencia_termistor / resistencia_fija) + (beta_termistor / temp_referencia))
    temp_actual = temp_actual - 273.15  # Conversión a grados Celsius

    # Mapeo del voltaje del potenciómetro a un rango de 0 a 30°C
    temp_deseada = (voltaje_potenciometro / vcc_ref) * 30

    # Cálculo de la diferencia entre la temperatura deseada y la actual
    diferencia = abs(temp_deseada - temp_actual)

    # Limitar la diferencia máxima a 5°C
    diferencia = min(diferencia, 5)

    # Control de los LEDs según la diferencia de temperatura
    if temp_deseada > temp_actual:
        led_rojo.value = diferencia / 5
        led_azul.value = 0
    elif temp_deseada < temp_actual:
        led_azul.value = diferencia / 5
        led_rojo.value = 0
    else:
        led_rojo.value = 0
        led_azul.value = 0

    # Imprimir resultados en consola
    print(f"Termistor: {voltaje_termistor:.3f} V, {temp_actual:.3f} °C")
    print(f"Potenciómetro: {temp_deseada:.2f} °C")

    time.sleep(1)  # Espera entre lecturas
