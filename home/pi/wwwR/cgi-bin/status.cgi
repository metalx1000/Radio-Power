#!/bin/bash
echo "Content-type: text/html"
echo ""

let s="$(ps aux|grep radiopower|grep -v "avahi-daemon"|wc -l)"
if [ $s -gt 1 ]
then
  echo -n "Running"
else
  echo -n "Stopped"
fi
