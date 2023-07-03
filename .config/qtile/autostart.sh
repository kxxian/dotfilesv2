#!/bin/sh

# Set wallpaper
~/.fehbg & 

# Send welcome notification
notify-send "Welcome, devx"

# udiskie
udiskie & 

# Fancy visuals (E.g: enable opacity) 
picom &
