#!/bin/bash

TODAY=$(date)
echo "this scan created on $TODAY"

TARGET=$1
DIRECTORY=${TARGET}_recon
echo "creating directory $DIRECTORY"
mkdir -p $DIRECTORY

nmap -sT $TARGET -p80 -T4 > $DIRECTORY/nmap.txt
echo "result nmap scap in $DIRECTORY/nmap.txt"

gobuster dir --url $TARGET --wordlist /usr/share/wordlists/dirb/small.txt > $DIRECTORY/gobuster.txt
echo "result of scan in $DIRECTORY/gobuster.txt"

echo "------------------------------------------------------"
echo "                    nmap scan                         "
cat $DIRECTORY/nmap.txt

echo "------------------------------------------------------"
echo "                   gobuster scan                      "
cat $DIRECTORY/gobuster.txt
