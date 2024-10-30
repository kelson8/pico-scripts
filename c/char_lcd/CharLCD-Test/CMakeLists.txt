# Generated Cmake Pico project file

cmake_minimum_required(VERSION 3.13)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Initialise pico_sdk from installed location
# (note this can come from environment, CMake cache etc)

# == DO NEVER EDIT THE NEXT LINES for Raspberry Pi Pico VS Code Extension to work ==
if(WIN32)
    set(USERHOME $ENV{USERPROFILE})
else()
    set(USERHOME $ENV{HOME})
endif()
set(sdkVersion 2.0.0)
set(toolchainVersion 13_2_Rel1)
set(picotoolVersion 2.0.0)
set(picoVscode ${USERHOME}/.pico-sdk/cmake/pico-vscode.cmake)
if (EXISTS ${picoVscode})
    include(${picoVscode})
endif()
# ====================================================================================
set(PICO_BOARD pico_w CACHE STRING "Board type")

# Pull in Raspberry Pi Pico SDK (must be before project)
include(pico_sdk_import.cmake)

project(CharLCD-Test C CXX ASM)

# Initialise the Raspberry Pi Pico SDK
pico_sdk_init()

# Add executable. Default name is the project name, version 0.1

add_executable(CharLCD-Test CharLCD-Test.c )

pico_set_program_name(CharLCD-Test "CharLCD-Test")
pico_set_program_version(CharLCD-Test "0.1")

# Modify the below lines to enable/disable output over UART/USB
pico_enable_stdio_uart(CharLCD-Test 0)
pico_enable_stdio_usb(CharLCD-Test 0)

# Add the standard library to the build
target_link_libraries(CharLCD-Test
        pico_stdlib)

# New
# https://github.com/hhoswaldo/pico-keypad4x4
# Add pico_keypad4x4 as a library to your project
add_library(keypad_4x4 STATIC "${CMAKE_CURRENT_SOURCE_DIR}")

# Link required libraries to keypad_4x4
target_link_libraries(keypad_4x4
    pico_stdlib
    hardware_timer
)

# Link required libraries to main executable
target_link_libraries(CharLCD-Test
    keypad_4x4
)

# End new

# Add the standard include files to the build
target_include_directories(CharLCD-Test PRIVATE
  ${CMAKE_CURRENT_LIST_DIR}
  ${CMAKE_CURRENT_LIST_DIR}/.. # for our common lwipopts or any other standard includes, if required
)

# Add any user requested libraries
target_link_libraries(CharLCD-Test 
        hardware_i2c
        
        )

pico_add_extra_outputs(CharLCD-Test)

