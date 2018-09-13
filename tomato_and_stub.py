from adafruit_circuitplayground.express import cpx
import time



while True:
    if cpx.button_a:
        while True:
            #tomatoes()
            tomato_count = 0
            def check_tomatoes():
                global tomato_count
                if tomato_count == 0:
                    cpx.pixels[1] = ((0, 0, 0))
                    cpx.pixels[2] = ((0, 0, 0))
                    cpx.pixels[3] = ((0, 0, 0))
                    cpx.pixels[4] = ((0, 0, 0))
                    cpx.pixels[5] = ((0, 0, 0))
                    cpx.pixels[6] = ((0, 0, 0))
                    cpx.pixels[7] = ((0, 0, 0))
                    cpx.pixels[8] = ((0, 0, 0))

                elif tomato_count == 1:
                    cpx.pixels[1] = ((3, 0, 0))
                    cpx.pixels[2] = ((0, 0, 0))
                    cpx.pixels[3] = ((0, 0, 0))
                    cpx.pixels[4] = ((0, 0, 0))
                    cpx.pixels[5] = ((0, 0, 0))
                    cpx.pixels[6] = ((0, 0, 0))
                    cpx.pixels[7] = ((0, 0, 0))
                    cpx.pixels[8] = ((0, 0, 0))

                elif tomato_count == 2:
                    cpx.pixels[1] = ((3, 0, 0))
                    cpx.pixels[2] = ((3, 0, 0))
                    cpx.pixels[3] = ((0, 0, 0))
                    cpx.pixels[4] = ((0, 0, 0))
                    cpx.pixels[5] = ((0, 0, 0))
                    cpx.pixels[6] = ((0, 0, 0))
                    cpx.pixels[7] = ((0, 0, 0))
                    cpx.pixels[8] = ((0, 0, 0))

                elif tomato_count == 3:
                    cpx.pixels[1] = ((3, 0, 0))
                    cpx.pixels[2] = ((3, 0, 0))
                    cpx.pixels[3] = ((3, 0, 0))
                    cpx.pixels[4] = ((0, 0, 0))
                    cpx.pixels[5] = ((0, 0, 0))
                    cpx.pixels[6] = ((0, 0, 0))
                    cpx.pixels[7] = ((0, 0, 0))
                    cpx.pixels[8] = ((0, 0, 0))

                elif tomato_count == 4:
                    cpx.pixels[1] = ((3, 0, 0))
                    cpx.pixels[2] = ((3, 0, 0))
                    cpx.pixels[3] = ((3, 0, 0))
                    cpx.pixels[4] = ((3, 0, 0))
                    cpx.pixels[5] = ((0, 0, 0))
                    cpx.pixels[6] = ((0, 0, 0))
                    cpx.pixels[7] = ((0, 0, 0))
                    cpx.pixels[8] = ((0, 0, 0))
                    
                elif tomato_count == 5:
                    cpx.pixels[1] = ((3, 0, 0))
                    cpx.pixels[2] = ((3, 0, 0))
                    cpx.pixels[3] = ((3, 0, 0))
                    cpx.pixels[4] = ((3, 0, 0))
                    cpx.pixels[5] = ((3, 0, 0))
                    cpx.pixels[6] = ((0, 0, 0))
                    cpx.pixels[7] = ((0, 0, 0))
                    cpx.pixels[8] = ((0, 0, 0))
                    
                elif tomato_count == 6:
                    cpx.pixels[1] = ((3, 0, 0))
                    cpx.pixels[2] = ((3, 0, 0))
                    cpx.pixels[3] = ((3, 0, 0))
                    cpx.pixels[4] = ((3, 0, 0))
                    cpx.pixels[5] = ((3, 0, 0))
                    cpx.pixels[6] = ((3, 0, 0))
                    cpx.pixels[7] = ((0, 0, 0))
                    cpx.pixels[8] = ((0, 0, 0))
                    
                elif tomato_count == 7:
                    cpx.pixels[1] = ((3, 0, 0))
                    cpx.pixels[2] = ((3, 0, 0))
                    cpx.pixels[3] = ((3, 0, 0))
                    cpx.pixels[4] = ((3, 0, 0))
                    cpx.pixels[5] = ((3, 0, 0))
                    cpx.pixels[6] = ((3, 0, 0))
                    cpx.pixels[7] = ((3, 0, 0))
                    cpx.pixels[8] = ((0, 0, 0))
                    
                elif tomato_count == 8:
                    cpx.pixels[1] = ((3, 0, 0))
                    cpx.pixels[2] = ((3, 0, 0))
                    cpx.pixels[3] = ((3, 0, 0))
                    cpx.pixels[4] = ((3, 0, 0))
                    cpx.pixels[5] = ((3, 0, 0))
                    cpx.pixels[6] = ((3, 0, 0))
                    cpx.pixels[7] = ((3, 0, 0))
                    cpx.pixels[8] = ((3, 0, 0))

                elif tomato_count == 9:
                    tomato_count = 0

            def green_light():
                cpx.pixels[0] = ((0, 3, 0))
                time.sleep(2) #change to set for longer
                cpx.pixels[0] = ((0, 0, 0))

            def blue_light():
                cpx.pixels[9] = ((0, 0, 3))
                time.sleep(2) #change to set for longer
                cpx.pixels[9] = ((0, 0, 3))

            def green_blink():
                cpx.pixels[0] = ((0, 3, 0))
                time.sleep(0.5)
                cpx.pixels[0] = ((0, 0, 0))
                time.sleep(0.5)

            def green_blinkfast():
                cpx.pixels[0] = ((0, 3, 0))
                time.sleep(0.25)
                cpx.pixels[0] = ((0, 0, 0))
                time.sleep(0.25)

            def blue_blink():
                cpx.pixels[9] = ((0, 0, 3))
                time.sleep(0.5)
                cpx.pixels[9] = ((0, 0, 0))
                time.sleep(0.5)

            def blue_blinkfast():
                cpx.pixels[9] = ((0, 0, 3))
                time.sleep(0.25)
                cpx.pixels[9] = ((0, 0, 0))
                time.sleep(0.25)

            while True:
                check_tomatoes()
                if cpx.button_a:
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
        
    elif cpx.button_b:
        while True:
            #naptime()
            cpx.pixels[7] = ((3, 0, 0))
            time.sleep(.2)
            cpx.pixels[7] = ((0, 0, 0))
            time.sleep(.2)
    else:
        cpx.pixels[2] = ((0, 0, 3))
        cpx.pixels[7] = ((0, 0, 0))
        time.sleep(.5)
        cpx.pixels[2] = ((0, 0, 0))
        cpx.pixels[7] = ((0, 0, 3))
        time.sleep(.5)