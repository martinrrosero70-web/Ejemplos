from machine import Pin
motor1_pin_a = Pin(12, Pin.OUT)
motor1_pin_b = Pin(13, Pin.OUT)

motor2_pin_a = Pin(18, Pin.OUT)
motor2_pin_b = Pin(19, Pin.OUT)


def carro_adelante():
    motor1_pin_a. on()
    motor1_pin_b. off()
    motor2_pin_a. on()
    motor2_pin_b. off()

def carro_atras():
    motor1_pin_a. off()
    motor1_pin_b. on()
    motor2_pin_a. off()
    motor2_pin_b. on()

def carro_izquierda():
    motor1_pin_a. off()
    motor1_pin_b. on()
    motor2_pin_a. on()
    motor2_pin_b. off()

def carro_derecha():
    motor1_pin_a. on()
    motor1_pin_b. off()
    motor2_pin_a. off()
    motor2_pin_b. on()

def carro_parar():
    motor1_pin_a. off()
    motor1_pin_b. off()
    motor2_pin_a. off()
    motor2_pin_b. off()
    