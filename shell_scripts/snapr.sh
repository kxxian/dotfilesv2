#!/bin/bash 

sudo timeshift --list

read "s?What snapshot do you want to restore? "

if [[ -z "$s" ]]; then 
  echo "FAILED. Enter a snapshot name to restore!"
else 
  sudo timeshift --restore --snapshot "$s"
  echo "DONE. Snapshot successfully restored!"
fi
