#!/bin/bash

init(){
  # Disable tap delay
  echo $(synclient ClickTime=0)
  echo $(synclient SingleTapTimeout=0)
  
  # Disable right click tap
  echo $(synclient RightButtonAreaLeft=0)
  echo $(synclient RightButtonAreaTop=0)
}

init
