#!/bin/sh

# Adam Anderson
# Aug 3, 2013

# Imports the options supplied by Logitech along 
# with uvcdynctrl to control more advanced webcams.
#
# This import requires root permissions, but only 
# needs to be called one time in order to set up 
# your system to include the new options from the 
# XML file.

sudo uvcdynctrl --import=/usr/share/uvcdynctrl/data/046d/logitech.xml