#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

import os
import signal
import commands
from subprocess import call
from gi.repository import Gtk
from gi.repository import AppIndicator3 as AppIndicator

APPINDICATOR_ID = "screenrotator"
TRACKPAD_ID = "13"
KEYBOARD_ID = "12"
orientation = "normal"

item_toggle_trackpad = ''
item_toggle_keyboard = ''

def main():
    indicator = AppIndicator.Indicator.new(APPINDICATOR_ID, '/home/barryels/Projects/linux-automation-scripts/ScreenRotator/icon.svg', AppIndicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    Gtk.main()

def build_menu():
    global item_toggle_trackpad
    global item_toggle_keyboard

    menu = Gtk.Menu()
    #brightness
    item_brightness_up = Gtk.MenuItem('Increase Brightness')
    item_brightness_up.connect('activate', increase_brightness)
    menu.append(item_brightness_up)
    item_brightness_down = Gtk.MenuItem("Decrease Brightness")
    item_brightness_down.connect('activate', decrease_brightness)
    menu.append(item_brightness_down)
    #rotate
    item_rotate = Gtk.MenuItem('Rotate')
    item_rotate.connect('activate', rotate_screen)
    menu.append(item_rotate)
    #flip
    item_flip = Gtk.MenuItem('Flip')
    item_flip.connect('activate', flip_screen)
    menu.append(item_flip)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #toggle trackpad & keyboard
    item_toggle_trackpad = Gtk.MenuItem('Toggle Trackpad...')
    item_toggle_trackpad.connect('activate', toggle_trackpad)
    menu.append(item_toggle_trackpad)
    item_toggle_keyboard = Gtk.MenuItem('Toggle Keyboard...')
    item_toggle_keyboard.connect('activate', toggle_keyboard)
    menu.append(item_toggle_keyboard)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #quit
    item_quit = Gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    update_menu_items()
    return menu

def rotate_screen(source):
    global orientation
    if orientation == "normal":
        direction = "left"
    elif orientation == "left":
        direction ="normal"
    call(["xrandr", "-o", direction])
    orientation = direction

def flip_screen(source):
    global orientation
    if orientation == "normal":
        direction = "inverted"
    elif orientation == "inverted":
        direction ="normal"
    call(["xrandr", "-o", direction])
    orientation = direction


def increase_brightness(source):
    call(["xbacklight", "-inc", "20"])

def decrease_brightness(source):
    call(["xbacklight", "-dec", "20"])


def toggle_trackpad(source):
    # call(["xinput", "set-prop 13 'Device Enabled' 0"])
    if get_trackpad_enabled_status() == '1':
        disable_trackpad()
    else:
        enable_trackpad()


def disable_trackpad():
    global TRACKPAD_ID
    call(["xinput", "disable", TRACKPAD_ID])
    update_menu_items()

def enable_trackpad():
    global TRACKPAD_ID
    call(["xinput", "enable", TRACKPAD_ID])
    update_menu_items()


def toggle_keyboard(source):
    if get_keyboard_enabled_status() == '1':
        disable_keyboard()
    else:
        enable_keyboard()

def disable_keyboard():
    call(["xinput", "disable", KEYBOARD_ID])
    update_menu_items()

def enable_keyboard():
    call(["xinput", "enable", KEYBOARD_ID])
    update_menu_items()



def get_trackpad_enabled_status():
    global TRACKPAD_ID
    # return call(["xinput", "list-props", "13", "|", "grep", "Device\ Enabled", "|", "sed", "-e", "'s/.*\:[ \t]\+//g'"])
    # status=`xinput list-props ${tpid} | grep Device\ Enabled | sed -e 's/.*\:[ \t]\+//g'`
    return commands.getstatusoutput("xinput list-props "+ TRACKPAD_ID +" | grep Device\ Enabled | sed -e 's/.*\:[ \t]\+//g'")[1]


def get_keyboard_enabled_status():
    global KEYBOARD_ID
    return commands.getstatusoutput("xinput list-props "+ KEYBOARD_ID +" | grep Device\ Enabled | sed -e 's/.*\:[ \t]\+//g'")[1]


def update_menu_items():
    if get_trackpad_enabled_status() == '1':
        item_toggle_trackpad.get_child().set_text('Disable Trackpad')
    else:
        item_toggle_trackpad.get_child().set_text('Enable Trackpad')

    if get_keyboard_enabled_status() == '1':
        item_toggle_keyboard.get_child().set_text('Disable Keyboard')
    else:
        item_toggle_keyboard.get_child().set_text('Enable Keyboard')


if __name__ == "__main__":
    #make sure the screen is in normal orientation when the script starts
    call(["xrandr", "-o", orientation])
    #keyboard interrupt handler
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
