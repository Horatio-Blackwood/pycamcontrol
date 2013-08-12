# Adam Anderson
# Depends on:  Python 3.2, uvcdynctrl
# August 12, 2013

import configparser
from webcam import *


class WebcamBuilder(object):
    """ A factory/builder that can construct a new Class/Type dynamically
        that includes the appropriate methods for the camera type defined
        by a WebcamConfig.
    """

    def buildWebcam(camConfig, debug=False):
        """ Dynamically constructs and returns an instance of a  Webcam 
            object that includes all of the methods that are appropriate 
            for the camera described bythe camera configuration.
        """
        
        ### Create Type, and set its debug flag.
        camType = type(camConfig.name)
        camType.debug = debug
        
        ### Add Methods
        cfgParser = configparser.RawConfigParser()
        cfgParser.read(camConfig)
        
        # Pan Relative
        if (cfgParser.getboolean("methods", "pan_relative")):
            camType.panLeftRelative = webcam.panLeftRelative
            camType.panRightRelative = webcam.panRightRelative
            
        # Tilt Relative
        if (cfgParser.getboolean("methdos", "tilt_relative")):
            camType.tiltDownRelative = webcam.tiltDownRelative
            camType.tiltUpRelative = webcam.tiltUpRelative

        # led mode
        if (cfgParser.getboolean("methods", "led1_mode")):
            camType.ledMode = webcam.ledMode
            
        # Pan Reset
        if (cfgParser.getboolean("methods", "pan_reset")):
            camType.panReset = webcam.panReset
        
        # Tilt Reset
        if (cfgParser.getboolean("methods", "tilt_reset")):
            camType.tiltReset = webcam.tiltReset

        return camType()
