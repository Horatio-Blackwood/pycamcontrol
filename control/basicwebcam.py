# Adam Anderson
# Depends on:  Python 3.2, uvcdynctrl
# August 3, 2013


class BasicWebcam:
	
	def __init__(self):
		""" A basic webcam that supports:
				Brightness
				Contrast
				Saturation
				Hue
				White Balance Temperature, Auto
				Gamma
				Power Line Frequency
				White Balance Temperature
				Sharpness
				Backlight Compensation
				Pan (Absolute)
				Tilt (Absolute)
				Zoom, Absolute
		"""
		self.name = "Basic Webcam"
