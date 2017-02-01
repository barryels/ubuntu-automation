#!/usr/bin/python

import sys
import os
import commands

#screenDimensions = os.system("xdpyinfo | grep dimensions | grep -o '[0-9x]*' | head -n1")
screenDimensions = commands.getstatusoutput("xdpyinfo | grep dimensions | grep -o '[0-9x]*' | head -n1")
#screenDimensions = os.system("xrandr | grep '*' | grep -o '[0-9x]*'")

screenDimensions = screenDimensions[1].split("x")


left = 0
top = 0
width = 800
height = 600
screenWidth = int(screenDimensions[0])
screenHeight = int(screenDimensions[1])

if "1" in sys.argv:
	width = 1680
	height = screenHeight
elif "2" in sys.argv:
	width = 1280
	height = screenHeight
	left = (screenWidth - width) / 2
else:
	width = screenWidth
	height = screenHeight
	print 'nothing'

os.system("wmctrl -r :ACTIVE: -b remove,maximized_horz,maximized,vert")
os.system("wmctrl -r :ACTIVE: -e 0," + str(left) + "," + str(top) + "," + str(width) + "," + str(height))

print str(left) + "," + str(top) + "," + str(width) + "," + str(height)

