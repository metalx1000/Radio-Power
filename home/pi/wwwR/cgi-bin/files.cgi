#!/bin/bash
echo -en "Content-Type: text/html\r\n\r\n"

ls -lha ../output/*.txt|awk '{print $9 "-" $6 " " $7 " " $8}'|sed 's/..\/output\///g'|tac|head
