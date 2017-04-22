from RPIO import PWM

servo = PWM.Servo()
While True:
  servo.set_servo(13, 1200)
  servo.set_servo(27, 1200)
