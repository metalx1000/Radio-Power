#!/bin/bash
echo "Content-type: text/html"
echo ""

eval $(echo "$QUERY_STRING"|awk -F'&' '{for(i=1;i<=NF;i++){print $i}}')
h=`/bin/busybox httpd -d $hi`
echo "hi=$h"

l=`/bin/busybox httpd -d $low`
echo "low=$l"

/usr/local/bin/radiopower "$l" "$h" &
