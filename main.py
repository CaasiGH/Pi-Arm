import time

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].set_pulse_width_range(400, 2500)

kit.servo[0].angle = 45
time.sleep(1)
kit.servo[0].angle = 90
time.sleep(1)
#kit.servo[0].angle = 135
#time.sleep(1)
kit.servo[0].angle = 180
time.sleep(1)
kit.servo[0].angle = 0