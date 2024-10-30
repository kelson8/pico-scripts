#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/i2c.h"

// New
#include <string.h>
#include "pico/binary_info.h"

// Pico keypad
#include "pico_keypad4x4.h"

#define LED_PIN 18
#define DELAY_MS 1000



/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 * Copyright (c) 2024 kelson8 - KelsonCraft
 *
 * SPDX-License-Identifier: BSD-3-Clause
 * All credit goes to Raspberry Pi for this code below, I have only modified it.
 * https://github.com/raspberrypi/pico-examples/blob/master/i2c/lcd_1602_i2c/lcd_1602_i2c.c
 */

/*
 * Begin code from lcd_1602_i2c.c
*/

/* Example code to drive a 16x2 LCD panel via a I2C bridge chip (e.g. PCF8574)

   NOTE: The panel must be capable of being driven at 3.3v NOT 5v. The Pico
   GPIO (and therefore I2C) cannot be used at 5v.

   You will need to use a level shifter on the I2C lines if you want to run the
   board at 5v.

   Connections on Raspberry Pi Pico board, other boards may vary.

   GPIO 4 (pin 6)-> SDA on LCD bridge board
   GPIO 5 (pin 7)-> SCL on LCD bridge board
   3.3v (pin 36) -> VCC on LCD bridge board
   GND (pin 38)  -> GND on LCD bridge board
*/
// commands
const int LCD_CLEARDISPLAY = 0x01;
const int LCD_RETURNHOME = 0x02;
const int LCD_ENTRYMODESET = 0x04;
const int LCD_DISPLAYCONTROL = 0x08;
const int LCD_CURSORSHIFT = 0x10;
const int LCD_FUNCTIONSET = 0x20;
const int LCD_SETCGRAMADDR = 0x40;
const int LCD_SETDDRAMADDR = 0x80;

// flags for display entry mode
const int LCD_ENTRYSHIFTINCREMENT = 0x01;
const int LCD_ENTRYLEFT = 0x02;

// flags for display and cursor control
const int LCD_BLINKON = 0x01;
const int LCD_CURSORON = 0x02;
const int LCD_DISPLAYON = 0x04;

// flags for display and cursor shift
const int LCD_MOVERIGHT = 0x04;
const int LCD_DISPLAYMOVE = 0x08;

// flags for function set
const int LCD_5x10DOTS = 0x04;
const int LCD_2LINE = 0x08;
const int LCD_8BITMODE = 0x10;

// flag for backlight control
const int LCD_BACKLIGHT = 0x08;

const int LCD_ENABLE_BIT = 0x04;

// By default these LCD display drivers are on bus address 0x27
static int addr = 0x27;

// Modes for lcd_send_byte
#define LCD_CHARACTER  1
#define LCD_COMMAND    0

#define MAX_LINES      2
#define MAX_CHARS      16

/*
 * LCD Commands
*/

/* Quick helper function for single byte transfers */
void i2c_write_byte(uint8_t val) {
#ifdef i2c_default
    i2c_write_blocking(i2c_default, addr, &val, 1, false);
#endif
}

void lcd_toggle_enable(uint8_t val) {
    // Toggle enable pin on LCD display
    // We cannot do this too quickly or things don't work
#define DELAY_US 600
    sleep_us(DELAY_US);
    // What exactly is this doing? Never used the "|" syntax like this in C
    i2c_write_byte(val | LCD_ENABLE_BIT);
    sleep_us(DELAY_US);
    // Never used this syntax before either.
    i2c_write_byte(val & ~LCD_ENABLE_BIT);
    sleep_us(DELAY_US);
}

// The display is sent a byte as two separate nibble transfers
void lcd_send_byte(uint8_t val, int mode) {
    uint8_t high = mode | (val & 0xF0) | LCD_BACKLIGHT;
    uint8_t low = mode | ((val << 4) & 0xF0) | LCD_BACKLIGHT;

    i2c_write_byte(high);
    lcd_toggle_enable(high);
    i2c_write_byte(low);
    lcd_toggle_enable(low);
}

void lcd_clear(void){
    lcd_send_byte(LCD_CLEARDISPLAY, LCD_COMMAND);
}

// Go to location on LCD
void lcd_set_cursor(int line, int position){
    int val = (line == 0) ? 0x80 + position : 0xC0 + position;
    lcd_send_byte(val, LCD_COMMAND);
}

// What does inline do in C?
static inline void lcd_char(char val){
    lcd_send_byte(val, LCD_CHARACTER);
}

void lcd_string(const char *s){
    while(*s){
        lcd_char(*s++);
    }
}

void lcd_init(){
    lcd_send_byte(0x03, LCD_COMMAND);
    lcd_send_byte(0x03, LCD_COMMAND);
    lcd_send_byte(0x03, LCD_COMMAND);
    lcd_send_byte(0x02, LCD_COMMAND);

    lcd_send_byte(LCD_ENTRYMODESET | LCD_ENTRYLEFT, LCD_COMMAND);
    lcd_send_byte(LCD_FUNCTIONSET | LCD_2LINE, LCD_COMMAND);
    lcd_send_byte(LCD_DISPLAYCONTROL | LCD_DISPLAYON, LCD_COMMAND);
    lcd_clear();
}

/*
 * End LCD Commands
*/

/* 
 * End code from lcd_1602_i2c.c
*/

/*
 * Copied from my blink.c test
 * LED Commands
*/

void toggleLed(){
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
}


/*
 * End LED Commands
*/

/*
 * Character Matrix commands
*/

// https://forums.raspberrypi.com/viewtopic.php?t=378421

// I will need to test this once I find the cables for it.
#define ROW1 8
#define ROW2 7
#define ROW3 6
#define ROW4 28
#define COL1 3
#define COL2 4
#define COL3 5


void init_pins(){
    // Initialize rows as inputs with pull-up resistors
    gpio_init(ROW1);
    gpio_init(ROW2);
    gpio_init(ROW3);
    gpio_init(ROW4);

    gpio_set_dir(ROW1, GPIO_IN);
    gpio_set_dir(ROW2, GPIO_IN);
    gpio_set_dir(ROW3, GPIO_IN);
    gpio_set_dir(ROW4, GPIO_IN);

    gpio_pull_up(ROW1);
    gpio_pull_up(ROW2);
    gpio_pull_up(ROW3);
    gpio_pull_up(ROW4);

    // Initialize columns as outputs, starting high
    gpio_init(COL1);
    gpio_init(COL2);
    gpio_init(COL3);

    gpio_set_dir(COL1, GPIO_IN);
    gpio_set_dir(COL2, GPIO_IN);
    gpio_set_dir(COL3, GPIO_IN);
    
    gpio_pull_up(COL1);
    gpio_pull_up(COL2);
    gpio_pull_up(COL3);
}

/*
 * End Character Matrix commands
*/




// I2C defines
// This example will use I2C0 on GPIO8 (SDA) and GPIO9 (SCL) running at 400KHz.
// Pins can be changed, see the GPIO function select table in the datasheet for information on GPIO assignments
#define I2C_PORT i2c0
// #define I2C_SDA 8
// #define I2C_SCL 9

#define I2C_SDA 0
#define I2C_SCL 1


#define NEW_TEST
int main()
{
#if !defined(i2c_default) || !defined(PICO_DEFAULT_I2C_SDA_PIN) || !defined(PICO_DEFAULT_I2C_SCL_PIN)
    #warning CharLCD-Test requires a board with I2C pins
#else

    bool toggleLedEnabled = false;

#ifdef NEW_TEST
    // Modified to use code from example.
    i2c_init(I2C_PORT, 100 * 1000);
    gpio_set_function(I2C_SDA, GPIO_FUNC_I2C);
    gpio_set_function(I2C_SCL, GPIO_FUNC_I2C);
    gpio_pull_up(I2C_SDA);
    gpio_pull_up(I2C_SCL);
#else
    // Code from lcd_1602_i2c.c
    // This example will use I2C0 on the default SDA and SCL pins (4, 5 on a Pico)
    i2c_init(i2c_default, 100 * 1000);

    gpio_set_function(PICO_DEFAULT_I2C_SDA_PIN, GPIO_FUNC_I2C);
    gpio_set_function(PICO_DEFAULT_I2C_SCL_PIN, GPIO_FUNC_I2C);
    gpio_pull_up(PICO_DEFAULT_I2C_SDA_PIN);
    gpio_pull_up(PICO_DEFAULT_I2C_SCL_PIN);
#endif // NEW_TEST    
    // Make the I2C pins available to picotool
    bi_decl(bi_2pins_with_func(PICO_DEFAULT_I2C_SDA_PIN, PICO_DEFAULT_I2C_SCL_PIN, GPIO_FUNC_I2C));

    // Initalize the display
    lcd_init();

    static char *message[] = 
        {
            "Welcome to", "KCNet Systems",
        };

    // Toggle the leds
    if (toggleLedEnabled) {
        toggleLed();
    }

    
#ifdef TEST
    // Initalize the keypad for the keypad matrix
    pico_keypad_init(4, 4, 16);
#endif //_TEST
    
    // Loop for program, "while 1" seems to be the same as "while true" in C.
    while (1) {
        for (uint m = 0; m < sizeof(message) / sizeof(message[0]); m += MAX_LINES){
            for (int line = 0; line < MAX_LINES; line++){
                lcd_set_cursor(line, (MAX_CHARS / 2) - strlen(message[m + line]) / 2);
                lcd_string(message[m + line]);
            }
            gpio_put(LED_PIN, 0);
            sleep_ms(DELAY_MS);
            gpio_put(LED_PIN, 1);
            sleep_ms(DELAY_MS);
            lcd_clear();
        }
    }

    // stdio_init_all();

    // I2C Initialisation. Using it at 400Khz.
    // i2c_init(I2C_PORT, 400*1000);
    
    // gpio_set_function(I2C_SDA, GPIO_FUNC_I2C);
    // gpio_set_function(I2C_SCL, GPIO_FUNC_I2C);
    // gpio_pull_up(I2C_SDA);
    // gpio_pull_up(I2C_SCL);
    // // For more examples of I2C use see https://github.com/raspberrypi/pico-examples/tree/master/i2c

    // while (true) {
    //     printf("Hello, world!\n");
    //     sleep_ms(1000);
    // }
#endif
}
