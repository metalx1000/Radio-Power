#!/bin/bash

#check if root
if [[ $EUID -ne 0 ]]; then
  echo "You must be a root user"
  echo "Trying to restart script as sudo"
  sudo $0 $@
  exit
fi

cp -vr home/pi/wwwR/* /home/pi/wwwR/
cp -vr usr/local/bin/* /usr/local/bin/
cp -vr etc/* /etc/

#set proper permissions
chmod -R 777 /home/pi/wwwR
chown -R pi:pi /home/pi/wwwR/*
chown -R pi:pi /home/pi/wwwR

