import RPi.GPIO as GPIO
import time
import os

def init_gpio():
    # SET THE GPIO PIN SELECTION NUMBERING USING THE MOTHERBOARD ORDER
    GPIO.setmode(GPIO.BOARD)

    # SET THE 7th GPIO PIN AS A PIN THAT SENDS ELECTRICAL SIGNALS 
    GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

def fan_operation():
    start = time.time()
    on = False
    while(True):
        # READ CPU TEMP
        temp = int(os.popen("cat /sys/class/thermal/thermal_zone*/temp").read())
        print("CPU temp:", str(temp / 1000), "C\n\n")

        # IF CPU TEMP HIGHER THAN 60 DEGREES TURN THE FAN ON, ELSE TURN THE FAN OFF 
        if temp / 1000 >= 60:
            if time.time() - start >= 5 and on is False:
                start = time.time()
                GPIO.output(7, GPIO.HIGH)
                on = True
        elif temp / 1000 < 50:
            GPIO.output(7, GPIO.LOW)
            on = False


if __name__ == "__main__":
    try:
        init_gpio()
        fan_operation()
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()