**CamState**<br>
The <i>CamState</i> object contains values that describe the current state of your camera.  Each time you make a call to a <i>Webcam</i> asking it to do something or change a setting, a <i>CamState</i> is returned that contains the entire state of the Camera.<br>
<br>
<br>

<b>Camera Configuration Files</b><br>
A configuration file/object for a given camera that lists out the operations that are valid for that camera.  Other important data that further describes specific camera models may also be stored in the <i>CameraConfiguration</i>.  (<i>This idea is not yet implemented</i>).<br>
<br>
<br>
<b>WebcamBuilder</b><br>
A class that takes a webcam configuration and dynamically generates a webcam object (a 'type') that can be used to control a physical webcam and returns an initialized instance of the dynamically generated type.<br>
<br>
<br>

<b>Webcam</b><br>
This term represents a "class" of object types that are generated dynamically based on webcam configurations by the <i>WebcamBuilder</i> object.