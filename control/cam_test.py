# adam anderson
# Depends on:  Python 3.2, uvcdynctrl
# Aug 2, 2013

from camstate import CamState
from orbitwebcam import OrbitWebcam
from orbitwebcam import LED_ON
from orbitwebcam import LED_OFF
from orbitwebcam import LED_BLINK
import time


def orbitTest(camstate):
    print("Basic Orbit Webcam Test")
    print("Initializing Orbit Webcam object...")
    orbit = OrbitWebcam(debug=False)
    print("Initialized.  ", orbit)

    print(" --- Reset Tilt ---------------- ")
    orbit.resetTilt(camstate)
    print(camstate)
    time.sleep(5)


    print(" --- Reset Pan ---------------- ")
    orbit.resetPan(camstate)
    print(camstate)
    time.sleep(5)
    

    print(" --- Testing LED Mode ---------------- ")
    print(" --- LED On ---")
    orbit.ledMode(camstate, LED_ON)
    print(camstate)
    time.sleep(5)
    

    print(" --- LED Blink --- ")
    orbit.ledMode(camstate, LED_BLINK)
    print(camstate)
    time.sleep(5)


    print(" --- LED Off ---- ")
    orbit.ledMode(camstate, LED_OFF)
    print(camstate)
    time.sleep(5)


def main():
    cs = CamState.new()
    print("Initializing new CamState.")
    print(cs)    
    orbitTest(cs)

main()
