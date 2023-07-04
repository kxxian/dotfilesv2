#!/bin/sh


# Rofi CMD
rofi -show window \
  -theme "$HOME/.config/rofi/config.rasi" \
  -location 0 \
  -theme-str 'window {width: 800px; height: 600px; padding: 10;}' \
  -kb-element-next j \
  -kb-element-prev k 
