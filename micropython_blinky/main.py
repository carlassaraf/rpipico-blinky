# Importo modulo que maneja los pines
from machine import Pin
# Importo modulo de control de tiempo
from time import sleep
# Importo funciones de manejo de memoria
from mem_man import *

# Mensajes para obtener informacion del uso de memoria

print("Bytes de Flash libres: {:.2f} MB".format(get_free_flash()))
print("Porcentaje libre de Flash: {:.2f}%".format(get_free_flash_percent()))

print("Bytes de RAM usados: {:.2f} KB".format(get_allocated_ram()))
print("Bytes totales de RAM: {:.2f} KB".format(get_total_ram()))
print("Bytes reservados de RAM para Micropython: {:.2f} KB".format(get_reserved_ram()))
print("Porcentaje de RAM no disponible: {:.2f}%".format(get_allocated_ram_percent()))

# Programa principal

# Configuro el GPIO25 como salida
led = Pin(25, Pin.OUT)

while True:
    # Conmuto el LED
    led.value(not led.value())
    # Demora
    sleep(.5)
