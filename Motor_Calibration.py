import RPi.GPIO as GPIO

def calibrate_throttle():

    """starts up the program to calibrate the motors"""
    GPIO.setmode(GPIO.BCM)
    chan_list = [27, 10, 5, 13]
    GPIO.setup(chan_list, GPIO.OUT)

    motor_one=GPIO.PWM(27, 50)
    motor_two=GPIO.PWM(10, 50)
    motor_three=GPIO.PWM(5, 50)
    motor_four=GPIO.PWM(13, 50)

    Power = 10
    motor_one.start(Power)
    motor_two.start(Power)
    motor_three.start(Power)
    motor_four.start(Power)
    print "Connect battery to ESC, wait for about 2 seconds: Beep-Beep tone should be emitted"

    raw_input("Press enter to continue: several beep tones should be emitted, representing the number of battery cells: followed by a long Beeeep")
    Power = 5
    motor_one.ChangeDutyCycle(Power)
    motor_two.ChangeDutyCycle(Power)
    motor_three.ChangeDutyCycle(Power)
    motor_four.ChangeDutyCycle(Power)
    print "motor at % power" 
    
    raw_input("Press enter to cleanup")    
    motor_one.stop()
    motor_two.stop()
    motor_three.stop()
    motor_four.stop()
    GPIO.cleanup()
    print "Clean up done"

calibrate_throttle()
