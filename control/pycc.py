# adam anderson
# Depends on:  Python 3.2, uvcdynctrl
# August 3, 2013

# Dependencies:
#
#    UVCDYNCTRL
#    Requires uvcdynctrl to be installed.  (sudo apt-get install uvcdynctrl)
#
#    After this, you need to import the logitech params in order to gain access to pan, tilt and zoom commands.
#       to do this:  'sudo uvcdynctrl --import=/usr/share/uvcdynctrl/data/046d/logitech.xml'
#
#    Once imported, you shouldn't need to to this again.
#
#
# The Location of the UVC Dynamic Control Program
# Installed using:  'sudo apt-get install uvcdynctrl'
UVCDYNCTRL_LOC = "/usr/bin/uvcdynctrl"


def printProcessResult(description, result):
    """ A method that prints out standard out and standard error from 
        subprocess.
    """
    out, err = result.communicate()
    print(description)
    print("    out:  ", out)
    print("    err:  ", err)