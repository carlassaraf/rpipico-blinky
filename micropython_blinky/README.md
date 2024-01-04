# micropython_blinky

Este ejemplo de blinky usa Micropython como lenguaje de programacion. Consiste en un archivo [mem_man.py](mem_man.py) que contiene funciones para obtener informacion sobre el uso de la memoria y un [main.py](main.py) con el programa principal que imprime informacion de la memoria y luego hace un parpadeo del LED en el GPIO25.

Como resumen del uso de la memoria:

- De los 2 MB de Flash, solo 1.36 MB estan disponibles.
	- 0.002 MB usados corresponden los dos archivos mencionados arriba.
	- Los otros 0.638 MB usados son del firmware de Micropython.
	- Esto corresponde a un 67.97% de Flash libre.
	
- De los 264 KB de SRAM, solo 187.58 KB estan disponibles.
	- 6.75 KB corresponden al uso de RAM del programa.
	- 72.42 KB quedan reservados para que Micropython funcione.
	- Esto corresponde a un 68.5% de SRAM libre.
