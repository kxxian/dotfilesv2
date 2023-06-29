#!/bin/sh

. $(dirname $0)/loading_bar.sh 


while true ; do
  echo "Welcome to Arch Maintenance Script!"
  echo ""

  # Custom loading bar
  loading_bar

  echo "[0] Check systemctl failed"
  echo "[1] Check journal"
  echo "[2] Check journal size"
  echo "[3] Clear journal"
  echo "[4] Check cache"
  echo "[5] Delete cache"
  echo "[6] Clear unwanted dependencies"
  echo "[7] Check orphans"
  echo "[8] Delete orphans"
  echo "[9] Check config"
  echo "[ysc] Delete yay cache"
  echo ""
  echo "||===================||"
  echo "|| type 'q' to quit ||"
  echo "|| 'cc' to clear     ||"
  echo "|| 'notes' for tips  ||"
  echo "||===================||"
  echo ""

  read "input?Select an input between 0..9: "
  echo ""

  case "$input" in 
    0 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      systemctl --failed 
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    1 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      sudo journalctl -p 3 -xb
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    2 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      du -sh /var/log/journal
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    3 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      sudo journalctl --vacuum-time=2weeks
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    "q" ) break ;;
    "cc" ) clear ;; 
    4 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      sudo du -sh .cache/
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    5 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      sudo rm -rf .cache/*
      sudo du -sh .cache/
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    6 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      yay -Yc
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    7 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      pacman -Qtdq
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    8 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      sudo pacman -Rns $(pacman -Qtdq)
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    9 ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      du -sh .config/
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n" ;; 
    "notes" ) 
      echo "||=============================||" 
      echo "              START"
      printf "\n"
      echo "Check updates once for every two or three days"
      echo "Clean package cache every 10-15 days" 
      echo "Check orphans and unwanted dependencies every 15 days"
      echo "Check cache dir and config dir every three weeks"
      echo "Check journal every once a month"
      printf "\n"
      echo "               END"
      echo "||=============================||" 
      printf "\n";; 
    "ysc" ) yay -Sc ; printf "\n" ;;
    "q" ) break ;;
    "cc" ) clear ;; 
    * ) 
      echo "||====================||"
      echo "|| Command not found! ||"
      echo "||====================||\n" 
      sleep 1
      clear ;;
  esac

  if [[ -z "$input" ]] ; then 
    echo ""
  fi

done

echo "Exiting..."
