#!/usr/bin/sh

# Check if the number of arguments ($#) is not equal to (-ne) 1

if [ $# -ne 1 ]; then
	echo "Usage: ./myawesomescript.sh <bit.ly_url>"
    exit 1
fi

curl -sI "$1" | grep -i "Location" | cut -d " " -f 2
