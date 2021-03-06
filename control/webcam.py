# Adam Anderson
# Depends on:  Python 3.2, uvcdynctrl
# Aug 3, 2013

# Language libraries
import subprocess

# Constant Values
from constants import UVCDYNCTRL_LOC
from constants import TILT_REL
from constants import PAN_REL
from constants import PAN_RESET
from constants import TILT_RESET
from constants import PAN_LEFT_MAX
from constants import PAN_RIGHT_MAX
from constants import TILT_UP_MAX
from constants import TILT_DOWN_MAX
from constants import LED_OFF
from constants import LED_ON
from constants import LED_BLINK
from constants import LED_AUTO

# Utility Methods
from pycc import printProcessResult


def tiltUpRelative(self, camState, amount):
    """ Tilts the camera up.
    """
    amt = amount * -1
    if (camState.tilt - amount) <= TILT_UP_MAX:
        amt = (camState.tilt - amount) - TILT_UP_MAX
        camState.tilt = TILT_UP_MAX
    else:
        camState.tilt = camState.tilt - amount

    result = subprocess.Popen([UVCDYNCTRL_LOC, "-s", TILT_REL, "--", str(amt)], stdout=subprocess.PIPE)
    if (self.debug):
        printProcessResult("Tilting up", result)


def tiltDownRelative(self, camState, amount):
    """ Tilts the camera down.
    """
    amt = amount
    if (camState.tilt + amount) >= TILT_DOWN_MAX:
        amt = (camState.tilt + amount) - TILT_DOWN_MAX
        camState.tilt = TILT_DOWN_MAX
    else:
        camState.tilt = camState.tilt + amount
         
    result = subprocess.Popen([UVCDYNCTRL_LOC, "-s", TILT_REL, "--", str(amt)], stdout=subprocess.PIPE)
    
    if (self.debug):
        printProcessResult("Tilting down", result)


def panLeftRelative(self, camState, amount):
    """ Pans the camera left.
    """
    amt = amount
    if (camState.pan + amount) >= PAN_LEFT_MAX:
        amt = (camState.pan + amount) - PAN_LEFT_MAX
        camState.pan = PAN_LEFT_MAX
    else:
        camState.pan = camState.pan + amount

    result = subprocess.Popen([UVCDYNCTRL_LOC, "-s", PAN_REL, "--", str(amt)], stdout=subprocess.PIPE)
    if (self.debug):
        printProcessResult("Panning left", result)

def panRightRelative(self, camState, amount):
    """ Pans the camera right.
    """
    amt = amount * -1
    if (camState.pan - amount) <= PAN_RIGHT_MAX:
        amt = (camState.pan - amount) - PAN_RIGHT_MAX
        camState.pan = PAN_RIGHT_MAX
    else:
        camState.pan = camState.pan + amount

    result = subprocess.Popen([UVCDYNCTRL_LOC, "-s", PAN_REL, "--", str(amt)], stdout=subprocess.PIPE)
    if (self.debug):
        printProcessResult("Panning right", result)
    
def resetTilt(self, cs):
    """
    """
    print(TILT_RESET)
    result = subprocess.Popen([UVCDYNCTRL_LOC, "-s", TILT_RESET, "0"], stdout=subprocess.PIPE)
    cs.tilt = 0           
    if (self.debug):
        printProcessResult("Resetting Tilt", result)
    
def resetPan(self, cs):
    """
    """
    print(PAN_RESET)
    result = subprocess.Popen([UVCDYNCTRL_LOC, "-s", TILT_REL, "3"], stdout=subprocess.PIPE)
    cs.pan = 0		
    if (self.debug):
        printProcessResult("Resetting Pan", result)
    

def ledMode(self, cs, option):
    """ Sets the mode of the LED on the camera.
    
        Parameters:
            cs - the current CamState object for this camera.
            option - the LED Mode to set the LED to.  Valid options are 
                     "0", "1", "2" or "3" meaning OFF, ON, BLINK or AUTO
                     respectively.
    """
    if (option != LED_ON and option != LED_OFF and 
    option != LED_BLINK and option != LED_AUTO):
        raise ValueError("Parameter 'option' must between 0 and 3.  Value was:  " + str(option))

    result = subprocess.Popen([UVCDYNCTRL_LOC, "-s", "LED1 Mode", str(option)], stdout=subprocess.PIPE)
    cs.ledState = option
    if (self.debug):
        printProcessResult("Setting LED mode", result)
           
def __str__(self):
    """ Returns a string that represents this object.
    """
    return "OrbitWebcam:  Debug = " + str(self.debug)
