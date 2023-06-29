#!/bin/sh 

# -n : do not append a newline
# -e : enable interpretation of backslash escapes
# \r : carriage return (go back to the beginning of the line without printing a newline)

loading_bar() {
  sleep 0.5
  echo -ne "Progress: [===                20%]\r"
  sleep 0.5
  echo -ne "Progress: [=======            40%]\r"
  sleep .05
  echo -ne "Progress: [=============      60%]\r"
  sleep .05
  echo -ne "Progress: [================   80%]\r"
  sleep .05
  echo -ne "Progress: [================== 100%]\r"
  sleep .05 
  printf "\n"
  echo "Loading complete...\n"
}
