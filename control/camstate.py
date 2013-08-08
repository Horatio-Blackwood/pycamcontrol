# Adam Anderson
# Depends on:  Python 3.2, uvcdynctrl
# August 2, 2013

import orbitwebcam

class CamState(object):
    """ An object that represents the current state of the web cam.
    """
    
    def __init__(self, pan=0, tilt=0, ledState=orbitwebcam.LED_OFF):
        """ Constructor.  Creates a new CamState.

            Parameters:
                pan      - the Left/Right position of the camera.
                tilt     - the Up/Down position of the camera.
                ledState - the state of the LED of the camera.  This parameter is for Orbit cameras only.
        """
        if (pan > 4480 or pan < -4480):
            raise ValueError("Pan must be between -4480 and 4480, inclusive.  Provided value was:  " +str(pan))

        if (tilt > 1920 or pan < -1920):
            raise ValueError("Tilt must be between -1920 and 1920, inclusive.  Provided value was:  " +str(tilt))

        if (option != LED_ON and option != LED_OFF and option != LED_BLINK and option != LED_AUTO):
            raise ValueError("Parameter 'option' must between 0 and 3.  Value was:  " + str(option))
        
        # Basic Webcam Options
        self.brightness = None
        self.contrast = None
        self.saturation = None
        self.hue = None
        self.whiteBalance = None
        self.gamma = None
        self.powerLineFrequency = None
        self.sharpness = None
        self.backlightCompensation = None
        self.pan = pan
        self.tilt = tilt
        self.zoom = None

        # Additional Fields for Orbit Webcams
        self.ledState = ledState

    @classmethod
    def new(cls):
        """ Returns a new instance of CamState with all default values.
        """
        return CamState()
        
#    @staticmethod
#    def new():
#        """ Example Static method
#        """
#        return somethingStatic

    def __str__(self):
        """ Returns a String representation of this CamState object.
        """
        return "CamState:  Pan:  " + str(self.pan) + ", tilt:  " + str(self.tilt) + ", LED:  " + str(self.ledState)
