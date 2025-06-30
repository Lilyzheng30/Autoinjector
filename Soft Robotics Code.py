from machine import ADC, Pin
from time import sleep, time

ISEMeter = ADC(Pin(27))
MyLED = Pin(16, Pin.OUT)         # LED for RobotA
RobotA = Pin(14, Pin.OUT)        # RobotA (on for 10s) air
RobotB = Pin(15, Pin.OUT)        # RobotB (on after 10s, off after 20s) water

consecutive_high_count = 0
threshold = 0.150
required_consecutive = 5

activated = False
activation_start_time = 0
robotb_start_time = 0
robotb_on = False

while True:
    if not activated:
        ISEvalue_counts = ISEMeter.read_u16()
        ISEvalue_volts = (ISEvalue_counts) * 3.3 / (2**16)
        print("Counts:", ISEvalue_counts)
        print("Volts:", ISEvalue_volts)

        if ISEvalue_volts > threshold:
            consecutive_high_count += 1
        else:
            consecutive_high_count = 0

        if consecutive_high_count >= required_consecutive:
            activated = True
            activation_start_time = time()

            # Turn on RobotA and LED immediately
            MyLED.value(1)
            RobotA.value(1)
            print("RobotA activated! RobotB will turn on in 10 seconds.")
    else:
        elapsed = time() - activation_start_time

        if elapsed >= 2 and not robotb_on:
            # Turn off RobotA and LED, turn on RobotB
            MyLED.value(0)
            RobotA.value(0)
            RobotB.value(1)
            robotb_on = True
            robotb_start_time = time()
            print("RobotA deactivated. RobotB activated for 20 seconds.")

        if robotb_on and (time() - robotb_start_time >= 20):
            RobotB.value(0)
            print("RobotB deactivated after 20 seconds.")
            break

    sleep(1)

print("Program finished.")
