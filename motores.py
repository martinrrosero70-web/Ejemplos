from machine import Pin
import time
from libmotor import carro_adelante, carro_atras, carro_derecha, carro_izquierda, carro_parar
carro_adelante()
time.sleep(2)
carro_parar()
