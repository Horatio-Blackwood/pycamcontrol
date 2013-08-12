# Adam Anderson
# Depends on:  Python 3.2, uvcdynctrl
# August 12, 2013
# constants.py


# The text for the relative tilt command.
TILT_REL = "Tilt (relative)"

# The text for the relative pan command.
PAN_REL = "Pan (relative)"

# The text for the Pan Reset command.
PAN_RESET = "Pan Reset"

# The text for the Tilt Reset command.
TILT_RESET = "Tilt Reset"

# Pan value rantges, as specified by uvcdynctrl -4480 to 4480
PAN_LEFT_MAX = 4480
PAN_RIGHT_MAX = -4480

# Tilt value ranges, as specified by uvcdynctrl:  -1920 to 1920
TILT_UP_MAX = -1920
TILT_DOWN_MAX = 1920

# LED States
LED_OFF = 0
LED_ON = 1
LED_BLINK = 2
LED_AUTO = 3

# The installed location of uvcdynctrl
UVCDYNCTRL_LOC = "/usr/bin/uvcdynctrl"
