import os

#path = os.path.dirname(os.path.realpath(__file__))
path = "~/Projects/linux-automation-scripts"
#path = os.getcwd()
system.exec_command("python "+ path +"/ResizeWindow/script.py")


#keyboard.send_keys("#: " + path)

#: ~/Projects/linux-automation-scripts/
#: /home/barryels

#from Tkinter import Tk
#from tkFileDialog import askopenfilename

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)


#baseDir = "~/Projects/linux-automation-scripts/ResizeWindow/"
#optionsDir = baseDir + "list/"

#options = os.listdir("/home/barryels/Projects/linux-automation-scripts/ResizeWindow/")

#returnCode, choice = dialog.list_menu(options, default='1280x100%.txt')
#returnCode, choice = dialog.choose_directory(initialDir='~/Projects')
#returnCode, choice = dialog.open_file()
#keyboard.send_keys("<ctrl>+l")

#if returnCode == 0:
#    keyboard.send_keys("You chose " + choice)



#if returnCode == 0:
#    keyboard.send_keys("You chose: '" + choice +"'")

#screenDimensions = system.exec_command("xdpyinfo | grep dimensions | grep -o '[0-9x]*' | head -n1")

#system.exec_command("wmctrl -r :ACTIVE: -b remove,maximized_horz,maximized_vert")
#system.exec_command("wmctrl -r :ACTIVE: -e 0,0,0,1680,800")

