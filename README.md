# pico-scripts

Python scripts and C/C++ code that I am playing with on the Raspberry Pi Pico. Licensed under MIT anyone is free to use these.

Check out the official Raspberry Pi pico-examples here: https://github.com/raspberrypi/pico-examples/

There are plently of examples that everyone can use to learn from there, it is where I have obtained a lot of my ideas that I have played around with.

Also check out the offical Raspberry Pi Pico guide here: https://projects.raspberrypi.org/en/projects/introduction-to-the-pico/0

I have documented where I have obtained most of these sources so by looking through the code there is links in most of the python files to check out.

## Contents

### C folder
* Blink LED - Modified version of the blink LED C code for turning on/off the onboard LED and a optional pin defined as LED_PIN in the code. Set the onboardLed boolean to true to enable the onboard LED.

* CharLCD-Test - Modified code from the pico-examples on the official Raspberry Pi github

### Python folder
Root folder:
* 7_segment_display.py - Demo with a 7 segment display, I never did get this one working myself.
* i2c_test.py - Show a list of I2C devices currently connected.
* lcd_api.py - Api for a 16x2 LCD.
* led_test.py - Test toggling LEDs and writing if they are on to the screen, could be improved.
* photo_sensor.py - Basic test with a photo resistor.
* pico_i2c_lcd - I2C 16x2 LCD support.
* temperature_test.py - Demo of the built in temperature sensor on the Raspberry Pi Pico

Lib folder:
* uping - Library for using ping with a Raspberry Pi Pico W, this will not work without the wifi model.

LCD folder:
* 16x2_lcd.py - Writing to a 16x2 LCD and clearing the screen
* clear_lcd.py - Clears the current 16x2 LCD screen.

Test folder:
* index.html - Basic html page for toggling a led on and off.
* lcd_wifi_display.py - Show if wifi is connected on the 16x2 LCD, and write the IP Address to the screen. Ping server test added which seems to work, I haven't hooked it up to the LCD yet. 
* ping_test.py - Ping using the uping library, print to the console or the screen in use.
* potentiometer_test.py - Show the values of a potentiometer on a LCD and print it out.
* secrets_example.py - Example file for the ssid and password being stored, secrets.py is in the gitignore so it won't show up.
* serial_connection.py - Basic serial connection test, tested with Raspberry Pi 3 and Raspberry Pi Pico being connected via UART/Serial.
* webserver_test.py - Basic webserver on Raspberry Pi Pico using a html file, redirects to index.html and is able to toggle LEDs on/off if configured.
* webserver_test_old.py - Another Basic webserver on Raspberry Pi Pico using a html file, this one doesn't work right
* wifi_connect.py - Connect to the wifi


## License
This project and its contents are licensed under the free and open source MIT license.
