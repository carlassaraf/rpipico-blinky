#include "pico/stdlib.h"

/**
 * @brief Programa principal
*/
int main(void) {
    // Inicializo GPIO25 (LED)  
    gpio_init(PICO_DEFAULT_LED_PIN);
    // Configuro GPIO25 como salida
    gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT);

    while (true) {
        // Cambio el estado del LED
        gpio_put(PICO_DEFAULT_LED_PIN, !gpio_get(PICO_DEFAULT_LED_PIN));
        // Demora
        sleep_ms(500);
    }
}
