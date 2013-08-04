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
                pan - the Left/Right position of the camera.
                tilt - the Up/Down position of the camera.
        """
        self.pan = pan
        self.tilt = tilt
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