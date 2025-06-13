#!/bin/bash

# Get the current date and time
TODAY=$(date)
echo "This scan was created on $TODAY"

# Get the target from the first argument
TARGET=$1

# Create a directory using the target name
DIRECTORY=$(basename "$TARGET")
echo "Creating directory $DIRECTORY"
mkdir -p "$DIRECTORY"

# Check the mode of operation
if [ "$2" = "nmap-only" ]; then
    nmap -sT "$TARGET" -p 80 -T4 > "$DIRECTORY/nmap.txt"
    echo "Result in $DIRECTORY/nmap.txt"
    cat "$DIRECTORY/nmap.txt"

elif [ "$2" = "gobuster-only" ]; then 
    gobuster dir --url "$TARGET" --wordlist /usr/share/wordlists/dirb/small.txt > "$DIRECTORY/gobuster.txt"
    echo "Result in $DIRECTORY/gobuster.txt"
    cat "$DIRECTORY/gobuster.txt"

else
    nmap -sT "$TARGET" -p 80 -T4 > "$DIRECTORY/nmap.txt"
    echo "Result in $DIRECTORY/nmap.txt"
    echo "----------------nmap------------------"
    cat "$DIRECTORY/nmap.txt"

    gobuster dir --url "$TARGET" --wordlist /usr/share/wordlists/dirb/small.txt > "$DIRECTORY/gobuster.txt"
    echo "Result in $DIRECTORY/gobuster.txt"
    echo "----------------gobuster------------------"
    cat "$DIRECTORY/gobuster.txt"
fi