**August 19, 2013**<br>
Started working on the cam_test.py file tonight.  Didn't get it finished, but started converting it to work with the type generation code.  This is giving me some grief, as I am new to the built-in type() function.<br>
<br>
<b>August 12, 2013</b><br>
On vacation right now, and I don't have access to a computer that has uvcdynctrl on it.  Started to define some classes that will support dynamically defining a webcam object based on a configuration file that defines the capabilities of that camera.  Will test and proof this when I have a Linux-based system.<br>
<br>
<br>
Note:  cam_test.py is not currently functional, as much of the code it was written against does not exist or has been heavily modified.  When I have a chance to test the new dynamic type definition, I'll re-work it to where it functions again.<br>
<br>
<b>August 7, 2013</b><br>
Tinkered a little bit with the CamState object.  I've been doing some thinking about how to organize the rest of the objects in the most useful way - it just hasn't manifested itself in code changes yet.  When I've got a more solid idea, it'll start to show up here.<br>
<br>
<b>August 4, 2013</b><br>
Wrote up some functionality for cam_test.py, a basic diagnostic test that demonstrated some of what pycamcontrol hopes to accomplish.  Still noted an issue with cam_test freezing up my raspberry pi tonight.  Currently there is no attempt to handle exceptions tossed when creating processes that execute uvcdynctrl commands.  I suspect the issue lies there.<br>
<br>
<b>August 3, 2013</b><br>
The project was created and some scraps of code from quick and dirty Raspberry Pi project were scraped together and uploaded.  As such - the code should not be expected to be complete or bug free.