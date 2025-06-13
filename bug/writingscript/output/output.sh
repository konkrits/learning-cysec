#!/bin/bash

echo "creating directory $1_recon"
mkdir $1_recon

nmap -sT $1 -p 80 -T4 > $1_recon/nmap
echo "Result of nmap scan are stored in $1_recon/nmap"

gobuster dir --url $1 --wordlist /usr/share/wordlists/dirb/small.txt --output $1_recon/gobuster --quiet -z
echo "Result of gobuster are stored in $1_recon/gobuster"


