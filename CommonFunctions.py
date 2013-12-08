#!/usr/bin/python
# A Class of Methods For Common Functions
#
# NOTE: Code Has Not Yet Been Parsed For Errors
#

# Method Overloading, First Method Will Allow Custom Delay (ms)
def takePicture(delay):
	# Return Statement Will Allow Return of Exit Code
	return system("raspistill -f -o currentpicture.png -t " + str(delay))

# Convenience Method, Takes Picture With Default Delay (5s)
def takePicture():
	return takePicture(5000)

# TODO: Add Printing Method (Possible lpr Use)
# NOTE: lpr Tested and Works
# -r Switch Needs Consideration, Will Make Things More Efficient, May Cause Problems On Printer Error
