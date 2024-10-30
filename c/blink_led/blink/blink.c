/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include "pico/stdlib.h"

// Pico W devices use a GPIO on the WIFI chip for the LED,
// so when building for Pico W, CYW43_WL_GPIO_LED_PIN will be defined
#ifdef CYW43_WL_GPIO_LED_PIN
#include "pico/cyw43_arch.h"
#endif

#ifndef LED_DELAY_MS
#define LED_DELAY_MS 1000
#endif

#define LED_DELAY1_MS 250

#define LED_PIN 18
// #define LED_PIN 24

// Perform initialisation
int pico_led_init(void) {
#if defined(PICO_DEFAULT_LED_PIN)
    // A device like Pico that uses a GPIO for the LED will define PICO_DEFAULT_LED_PIN
    // so we can use normal GPIO functionality to turn the led on and off
    gpio_init(PICO_DEFAULT_LED_PIN);
    gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT);
    return PICO_OK;
#elif defined(CYW43_WL_GPIO_LED_PIN)
    // For Pico W devices we need to initialise the driver etc
    return cyw43_arch_init();
#endif
}

// Turn the led on or off
void pico_set_led(bool led_on) {
#if defined(PICO_DEFAULT_LED_PIN)
    // Just set the GPIO on or off
    gpio_put(PICO_DEFAULT_LED_PIN, led_on);
#elif defined(CYW43_WL_GPIO_LED_PIN)
    // Ask the wifi "driver" to set the GPIO on or off
    cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, led_on);
#endif
}

// Modifed with this guide:
// https://www.raspberrypi.com/news/how-to-blink-an-led-with-raspberry-pi-pico-in-c/
int main() {

    bool onboardLed = false;

    // Setup code for onboard LED. 
    if (onboardLed){
        int rc = pico_led_init();
        hard_assert(rc == PICO_OK);
    // Setup code for external LED attached to pin specified above.
    } else {
        gpio_init(LED_PIN);
        gpio_set_dir(LED_PIN, GPIO_OUT);
    }

    while (true) {
        // Run the onboard LED if true
        if(onboardLed){
            pico_set_led(true);
            sleep_ms(LED_DELAY_MS);
            pico_set_led(false);
            sleep_ms(LED_DELAY_MS);
        // Blink the external LED attachted to LED_PIN if false.
        } else {
            gpio_put(LED_PIN, 0);
            sleep_ms(LED_DELAY_MS);
            gpio_put(LED_PIN, 1);
            sleep_ms(LED_DELAY_MS);
        }

    }
}
