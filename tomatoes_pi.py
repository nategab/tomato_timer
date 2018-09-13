import RPi.GPIO as GPIO
import time

green_led = 4
blue_led = 17
red1_led = 27
red2_led = 24
red3_led = 12
switch_pin = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(red1_led, GPIO.OUT)
GPIO.setup(red2_led, GPIO.OUT)
GPIO.setup(red3_led, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

tomato_count = 0

def check_tomatoes():
    global tomato_count
    if tomato_count == 0:
        GPIO.output(red1_led, False)
        GPIO.output(red2_led, False)
        GPIO.output(red3_led, False)

    elif tomato_count == 1:
        GPIO.output(red1_led, True)
        GPIO.output(red2_led, False)
        GPIO.output(red3_led, False)

    elif tomato_count == 2:
        GPIO.output(red1_led, True)
        GPIO.output(red2_led, True)
        GPIO.output(red3_led, False)

    elif tomato_count == 3:
        GPIO.output(red1_led, True)
        GPIO.output(red2_led, True)
        GPIO.output(red3_led, True)

    elif tomato_count == 4:
        tomato_count = 0

def green_light():
    GPIO.output(green_led, True)
    time.sleep(2) #change to set for longer
    GPIO.output(green_led, False)

def green_blink():
    GPIO.output(green_led, True)
    time.sleep(0.5)
    GPIO.output(green_led, False)
    time.sleep(0.5)

def green_blinkfast():
    GPIO.output(green_led, True)
    time.sleep(0.25)
    GPIO.output(green_led, False)
    time.sleep(0.25)

def blue_light():
    GPIO.output(blue_led, True)
    time.sleep(2) #change to set for longer
    GPIO.output(blue_led, False)

def blue_blink():
    GPIO.output(blue_led, True)
    time.sleep(0.5)
    GPIO.output(blue_led, False)
    time.sleep(0.5)

def blue_blinkfast():
    GPIO.output(blue_led, True)
    time.sleep(0.25)
    GPIO.output(blue_led, False)
    time.sleep(0.25)

while True:
    check_tomatoes()
    GPIO.output(green_led, False)
    GPIO.output(blue_led, False)
    if GPIO.input(switch_pin) == False:
        print("starting tomatoes")
        print("green light on")
        green_light()
        print("green light blinking")
        for i in range(2): # change
            green_blink()
        for i in range(2): # change
            green_blinkfast()
        print("blue light on")
        blue_light()
        print("blue light blinking")
        for i in range(2): #change
            blue_blink()
        for i in range(2): #change
            blue_blinkfast()
        tomato_count = tomato_count + 1
        check_tomatoes()
