#!/bin/bash
echo "Content-type: text/plain"
echo ""

#get the last 2 lines of current output
ls ../output/*.html|tail -n2|while read file;
do 
  tail -n 1 "$file";
done
