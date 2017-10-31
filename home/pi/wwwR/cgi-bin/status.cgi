#!/bin/bash
echo "Content-type: text/html"
echo ""

let s="$(ps aux|grep radiopower|wc -l)"
if [ $s -gt 1 ]
then
  echo -n "Running"
else
  echo -n "Stopped"
fi
