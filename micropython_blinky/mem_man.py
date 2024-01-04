import gc
import os

# Equivalente en bytes de 1KB
SIZE_1KB = 1024
# Equivalente en bytes de 1MB
SIZE_1MB = 1048576
# Tamaño en KB de la SRAM del RP2040
RP2040_SRAM_SIZE_KB = 264
# Tamaño en MB del on board flash de la Raspberry Pi Pico
RPI_PICO_FLASH_SIZE_MB = 2

def get_free_flash():
    """
    Obtiene la memoria flash libre en MB
    """
    # Obtiene el estado del filesystem
    filesystem_stat = os.statvfs("/")
    # Obtiene el tamaño de los bloques del filesystem y la cantidad de bloques libres
    return (filesystem_stat[0] * filesystem_stat[3]) / SIZE_1MB


def get_free_flash_percent():
    """
    Obtiene el porcentaje de flash usado
    """
    # Devuelve el porcentaje usado
    return 100 * get_free_flash() / RPI_PICO_FLASH_SIZE_MB


def get_allocated_ram():
    """
    Obtiene la cantidad de memoria RAM ocupada en KB
    """
    # Reclama cualquier memoria libre
    gc.collect()
    # Devuelve la memoria ocupada
    return gc.mem_alloc() / SIZE_1KB


def get_free_ram():
    """
    Obtiene la cantidad de memoria RAM libre en KB
    """
    # Reclama cualquier memoria libre
    gc.collect()
    # Obtengo la memoria libre
    return gc.mem_free() / SIZE_1KB


def get_total_ram():
    """
    Obtiene la cantidad de memoria RAM total en KB
    """
    return get_free_ram() + get_allocated_ram()


def get_reserved_ram():
    """
    Obtiene la cantidad de memoria RAM reservada en KB
    """
    return RP2040_SRAM_SIZE_KB - get_free_ram() - get_allocated_ram()


def get_allocated_ram_percent():
    """
    Obtiene el porcentaje no disponible de RAM
    """
    return 100 * (get_allocated_ram() + get_reserved_ram()) / (get_total_ram() + get_reserved_ram())
