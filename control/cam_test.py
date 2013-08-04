# adam anderson
# Depends on:  Python 3.2, uvcdynctrl
# Aug 2, 2013

from camstate import CamState
from orbitwebcam import OrbitWebcam
from orbitwebcam import LED_ON


def main():
    cs = CamState.new()
    print(cs)
    
    orbit = OrbitWebcam(debug=True)
    print(orbit)
    
    orbit.ledMode(cs, LED_ON)

main()