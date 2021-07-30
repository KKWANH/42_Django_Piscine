#   42 KKIM - DJANGO & PYThON PISCINE - HEADER
#		finish date: 7/27
#		passed date: 7/29

#!/bin/sh
curl -Is $1 | grep "Location" | cut -d " " -f 2