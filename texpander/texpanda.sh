#!/bin/bash

# Version: 1.1.1
# Release: November 22, 2016


REQUIRED_MODULES="xdotool xclip zenity"

KEY=$1


init(){
  for MODULE in $REQUIRED_MODULES; do 
    which $MODULE &>/dev/null || {
      read -p "install the following required utils? : $REQUIRED_MODULES (y/n)" reply
      [[ "$reply" == "y" ]] && sudo apt-get install ${REQUIRED_MODULES}; 
    }
  done
  return 0
}


get_path_to_me(){
  echo "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/list/"
}


clipboard_paste(){
  pid=$(xdotool getwindowfocus getwindowpid)
  proc_name=$(cat /proc/$pid/comm)
  
  if [[ $proc_name =~ (terminal|terminator) ]]
  then
    xdotool key ctrl+shift+v
  else
    xdotool key ctrl+v
  fi
}


run_snippet(){
  base_dir=$(get_path_to_me)
  abbrvs=$(ls $base_dir)
  name=$(zenity --list --title=Texpander --column=Abbreviations $abbrvs)
  path=$base_dir$name

  if [[ $name ]]
  then

    if [ -e "$path" ]
    then
      clipboard=$(xclip -selection clipboard -o)
      xclip -selection c -i "$path"

      clipboard_paste

      sleep 0.1s

      echo $clipboard | xclip -selection c
    else
      zenity --error --text="Abbreviation not found:\n$name"
    fi
  fi
}


run_script(){
  local input_key=$1
  local output_key=""

  case $input_key in
    end)
      output_key="End" ;;
    end-with-select)
      output_key="--Shift_L+End" ;;
  esac

  echo ${output_key}
                
  # xdotool getactivewindow key ${output_key}
  # xdotool keydown Shift_L
  # xdotool getactivewindow key End
  # xdotool getactivewindow keyup Shift_L
  # xdotool keyup End
  # xdotool mousemove 1920 100
  # xdotool key --clearmodifiers shift+End
  # xdotool key --clearmodifiers End
  # xdotool keyup --clearmodifiers shift
  # xdotool search --class terminal windowactivate
  
}


run(){
  if [[ $KEY ]]
  then
    run_script $KEY
  else 
    run_snippet
  fi 
}


init && run
