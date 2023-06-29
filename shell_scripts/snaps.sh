#!/bin/bash

read "c?Enter a comment for the snapshot: "

if [ -z "$c" ] ; then 
  echo "FAILED. Enter a comment for the snapshot!"
else 
  sudo timeshift --create --comments "$c"
  sudo timeshift --list
  sudo grub-mkconfig -o /boot/grub/grub.cfg 
  echo "DONE. Snapshot $c created!"
fi
