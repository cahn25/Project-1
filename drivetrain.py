import wpilib #terminal

import os
from wpilib import TimedRobot, Joystick, Spark # joystick = GenericHID (human interface device)
from wpilib.drive import DifferentialDrive
from robot import MyRobot

class Drivetrain:

def __init__(self):
    self.left_motor = Spark(0)
    self.right_motor = Spark(1)
    self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)

def move(self, for, rot)
    forward = self.controller.getRawAxis(0)  # not self.forward because you wont need it somewhere else, not an essential quality that needs tracking
    rotate = self.controller.getRawAxis(1)
    self.drivetrain.arcadeDrive(forward, rotate)

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


