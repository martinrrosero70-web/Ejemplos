# Ejemplos
Analog.py EXPLICACION: 
el código lee continuamente el voltaje de un potenciómetro, lo convierte en un valor digital y muestra ese valor en la consola
 Explicación por partes
 Importaciones:from machine import ADC, Pin: Importa las clases necesarias para manejar pines digitales (Pin) y el Conversor Analógico-Digital (ADC).import time: Importa la librería para usar funciones de tiempo, como la pausa (sleep).
 Configuración de Pin:POT_PIN = 36: Define la constante para el pin donde está conectado el potenciómetro (Pin GPIO 36).pot = Pin(POT_PIN): Crea un objeto Pin para el pin 36.adc_pot = ADC(pot): Inicializa el Conversor Analógico-Digital (ADC) para leer valores analógicos de ese pin.Configuración del ADC:adc_pot.width(ADC.WIDTH_12BIT): Configura la resolución de la lectura a 12 bits, lo que significa que el valor digital resultante estará entre 0 y $2^{12} - 1$ (o sea, 0 a 4095).adc_pot.atten(ADC.ATTN_11DB): Configura la atenuación a 11dB, lo que generalmente permite medir voltajes de hasta 3.3V, que es el rango completo para el potenciómetro.
 Bucle Principal (while True):valor_pot = adc_pot.read(): Lee el valor analógico del potenciómetro, lo convierte a digital (entre 0 y 4095) y lo guarda en la variable valor_pot.print(f"Valor POT : {valor_pot}"): Imprime el valor leído en la consola.time.sleep(0.1): Hace una pausa de 100 milisegundos (0.1 segundos) antes de tomar la siguiente lectura.
En resumen, al girar la perilla del potenciómetro, el valor impreso en la consola cambiará en tiempo real entre 0 y 4095.

Leds.py EXPLICACION
realizar una secuencia simple de encendido y apagado de varios LEDs, aunque tiene un error de sintaxis en su implementación.

Función: Intenta encender y apagar brevemente cuatro LEDs conectados secuencialmente a los pines 12, 18, 19 y 13.

Mecanismo: Configura cada pin como salida (Pin.OUT) y usa la función led.value() para cambiar su estado.

Propósito: Demuestra la capacidad del microcontrolador para activar dispositivos externos, creando una secuencia temporizada.

 Secuencia Repetitiva de Salidas (Semáforo)
El tercer código es el más completo y representa la implementación de un semáforo o una secuencia de luces repetitiva.

Función: Ejecuta un ciclo continuo de tres luces (Rojo, Amarillo, Verde) conectadas a los pines 2, 4 y 18.

Mecanismo: Dentro de un bucle infinito (while True), la secuencia se desarrolla en tres etapas:

Enciende el Rojo y apaga los demás. Espera 1 segundo.

Enciende el Amarillo y apaga los demás. Espera 1 segundo.

Enciende el Verde y apaga los demás. Espera 1 segundo.

Propósito: Es un ejemplo clásico de cómo usar un microcontrolador para manejar eventos con tiempos definidos, controlando múltiples salidas de manera coordinada.

LIBMOTOR.PY EXPLICACION:
El código inicializa cuatro pines del microcontrolador (Pines 12, 13, 18, y 19) como salidas (Pin.OUT). Estos pines están conectados a un driver de motor (Puente H), el cual a su vez controla dos motores, denominados aquí Motor 1 y Motor 2. Para cambiar la dirección de un motor, el Puente H requiere que se activen sus dos pines de entrada en un patrón específico (uno en alto/ON y otro en bajo/OFF).

El código define cinco funciones que manipulan los estados (ON/OFF) de estos cuatro pines para lograr un movimiento coordinado:

Las funciones carro_adelante() y carro_atras() activan ambos motores en la misma dirección (hacia adelante o hacia atrás).

Las funciones carro_izquierda() y carro_derecha() realizan un giro en el sitio o sobre un eje. Para girar, el código invierte la dirección de un motor respecto al otro (por ejemplo, el Motor 1 avanza y el Motor 2 retrocede), lo que hace que el carro rote.

Finalmente, la función carro_parar() desactiva todos los pines de control, deteniendo la corriente y frenando ambos motores.

En resumen, el código crea una interfaz de alto nivel (las cinco funciones) que simplifica la compleja tarea de controlar los cuatro pines de bajo nivel, permitiendo a un programa principal llamar a una sola función como carro_adelante() para ejecutar un movimiento complejo.

MOTORES.PY EXPLICACION:
es un programa de prueba muy conciso cuyo único propósito es ejecutar una secuencia de movimiento predefinida en el robot móvil, utilizando las funciones de control de motor definidas previamente en el módulo libmotor.

El script primero realiza las importaciones necesarias: Pin y time de las librerías estándar de MicroPython, y crucialmente, importa las funciones de movimiento (carro_adelante, carro_parar, etc.) que residen en un archivo externo llamado libmotor. Una vez importadas, el programa llama a la función carro_adelante(), lo que activa los pines del controlador para que ambos motores comiencen a girar en la dirección de avance. Inmediatamente después, el programa se pausa durante 2 segundos (time.sleep(2)), permitiendo que el robot se desplace hacia adelante durante esa duración. Finalmente, el programa llama a carro_parar(), lo que desactiva todos los pines de control de los motores, deteniendo el robot por completo y finalizando la secuencia. Este tipo de script es fundamentalmente una prueba unitaria para confirmar que la configuración del hardware y las funciones de la librería (libmotor.py) funcionan correctamente juntas.

OLED. PY EXPLICACION:
Este código está diseñado para inicializar y mostrar texto en una pequeña pantalla OLED (SSD1306) utilizando la comunicación I2C con un microcontrolador (probablemente un ESP32 o Pyboard). El script primero realiza las importaciones necesarias, incluyendo la clase SSD1306 para controlar la pantalla. Luego, inicializa la interfaz I2C en el bus 0, asumiendo que los pines de reloj (scl) y datos (sda) están definidos previamente, y establece la frecuencia de comunicación. A continuación, el código escanea el bus I2C e imprime las direcciones de los dispositivos encontrados, lo que sirve para confirmar que la pantalla está conectada y accesible . Una vez que se confirma la conexión, se crea un objeto para la pantalla, definiendo sus dimensiones como 128 píxeles de ancho por 64 de alto. Finalmente, el código utiliza el objeto oled para limpiar la pantalla (oled.fill(0)), escribe los mensajes "Mocosos feos" y ":3" en posiciones específicas de la memoria interna, y luego utiliza el comando oled.show() para enviar esos datos de la memoria y visualizarlos en la pantalla física. En esencia, es un código de configuración y prueba para desplegar mensajes estáticos en un display.

RGBNEOPIXEL.PY EXPLICACION:
Este código tiene la intención de controlar una tira de luces LED Neopixel (WS2812), también conocidas como LEDs direccionables, utilizando un microcontrolador. El script comienza importando las librerías necesarias (machine, time, neopixel) y define las constantes para el pin de control (Pin 4) y la cantidad de píxeles a controlar (3 píxeles). Luego, inicializa el objeto neopixel (np) en ese pin y para esa cantidad de LEDs. A continuación, intenta asignar colores a los tres píxeles utilizando la notación RGB (Rojo, Verde, Azul, con valores de 0 a 255): el primer píxel se establece en blanco puro ((255, 255, 255)); el segundo píxel se intenta establecer en verde puro, pero hay un error de sintaxis al usar paréntesis (np(1)) en lugar de corchetes (np[1]); y el tercer píxel se establece en un blanco muy tenue. Finalmente, la llamada a np.write() es crucial, ya que envía los datos de color almacenados en la memoria del microcontrolador al bus de datos de los Neopixels, haciendo que los LEDs cambien su color visible.