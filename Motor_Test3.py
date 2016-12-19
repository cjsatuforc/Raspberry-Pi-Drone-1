import RPi.GPIO as GPIO
import time

def running_motor3():

    """starts up the program to test the motor"""
    GPIO.setmode(GPIO.BCM)
    chan_list = [27, 10, 5, 13]
    GPIO.setup(chan_list, GPIO.OUT)

    motor_one=GPIO.PWM(27, 50)
    motor_two=GPIO.PWM(10, 50)
    motor_three=GPIO.PWM(5, 50)
    motor_four=GPIO.PWM(13, 50)

    motor_one.start(5)
    motor_two.start(5)
    motor_three.start(5)
    motor_four.start(5)
    print "connect battery to ESC: then wait for long beeeeep"

    raw_input("Press enter to increase power.")
    Power = 6
    motor_one.ChangeDutyCycle(Power)
    motor_two.ChangeDutyCycle(Power)
    motor_three.ChangeDutyCycle(Power)
    motor_four.ChangeDutyCycle(Power)
    print "motor at % power" 
    
    raw_input("Press enter to terminate.")
    Power = 5
    motor_one.ChangeDutyCycle(Power)
    motor_two.ChangeDutyCycle(Power)
    motor_three.ChangeDutyCycle(Power)
    motor_four.ChangeDutyCycle(Power)
    print "terminated"
    
    raw_input("Press enter to cleanup")    
    motor_one.stop()
    motor_two.stop()
    motor_three.stop()
    motor_four.stop()
    GPIO.cleanup()
    print "Clean up done"

running_motor3()
