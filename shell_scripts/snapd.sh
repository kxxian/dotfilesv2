#!/bin/bash

re="^[0-9]+$"

sudo timeshift --list
read "n?How many snapshot you want to delete? "

if [[ -z "$n" ]] ; then
  echo "Error. Enter how many snapshots to delete!"
elif ! [[ "$n" =~ "$re" ]]; then 
  echo "Error. Not a number!"
else
  for (( i=0; i < n; i++ )) ; do
    read "d?Enter a name of snapshot you want to delete: " 

    if [[ -z "$d" ]] ; then
      echo "FAILED. Enter a name of snapshot you want to delete!"
      break
    else 
      sudo timeshift --delete --snapshot "$d"
      sudo grub-mkconfig -o /boot/grub/grub.cfg
      echo "DONE. Snapshot $d deleted!"
    fi
    sudo timeshift --list
  done
fi
