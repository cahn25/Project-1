import wpilib #terminal

import os
from wpilib import DigitalInput
from wpilib import TimedRobot, Joystick, Spark # joystick = GenericHID (human interface device)
from robot import MyRobot

class LineFollower:

def __init__(self, drivetrain):
    self.left_sensor = DigitalInput(8)
    self.right_sensr = DigitalInput(9)
    self.drivetrain = drivetrain
    # initilize sensors, 8 and 9

def run(self):
    left_data = self.left_sensor.get()
    right_data = self.right_sensor.get()
        if left_data:
            self.left_motot.move()
        elif right_data:
            self.right_motor.move()
      
    # logic and motor setting
    #if left sensor sees line, move left
    #if right sensor sees the line, move right
    #if neither see the line, move forward
def robotPeriodic(self):
'''This is called every cycle of the code. In general the code is loop
through every .02 seconds.'''
    pass

def autonomousInit(self):
'''This is called once when the robot enters autonomous mode.'''
    pass

def autonomousPeriodic(self):
'''This is called every cycle while the robot is in autonomous.'''
    pass

def teleopInit(self):
'''This is called once at the start of Teleop.'''
    pass

def teleopPeriodic(self):
'''This is called once every cycle during Teleop'''
    forward = self.controller.getRawAxis(0) # not self.forward because you wont need it somewhere else, not an essential quality that needs tracking
    rotate = self.controller.getRawAxis(1)
    self.drivetrain.arcadeDrive(forward, rotate)
    pass

if __name__ == "__main__"
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(Tony_The_Robot)


