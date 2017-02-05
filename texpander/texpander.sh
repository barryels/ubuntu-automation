#!/bin/bash

# Version: 1.1.1
# Release: November 22, 2016


REQUIRED_MODULES="xdotool xclip zenity"


init(){
  for MODULE in $REQUIRED_MODULES; do 
    which $MODULE &>/dev/null || {
      read -p "install the following required utils? : $REQUIRED_MODULES (y/n)" reply
      [[ "$reply" == "y" ]] && sudo apt-get install ${REQUIRED_MODULES}; 
    }
  done
  return 0
}


run(){
  base_dir="${HOME}/.texpander/"
  abbrvs=$(ls $base_dir)
  name=$(zenity --list --title=Texpander --column=Abbreviations $abbrvs)
  path=$base_dir$name

  if [[ $name ]]
  then

    if [ -e "$path" ]
    then
      clipboard=$(xclip -selection clipboard -o)
      xclip -selection c -i "$path"

      paste

      sleep 1s

      echo $clipboard | xclip -selection c
    else
      zenity --error --text="Abbreviation not found:\n$name"
    fi
  fi
}


paste(){
  pid=$(xdotool getwindowfocus getwindowpid)
  proc_name=$(cat /proc/$pid/comm)
  
  if [[ $1 =~ (terminal|terminator) ]]
  then
    xdotool key ctrl+shift+v
  else
    xdotool key ctrl+v
  fi
}

init && run
