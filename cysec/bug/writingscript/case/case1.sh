#!/bin/bash

TODAY=$(date)
echo "this scan was created $TODAY"

TARGET=$1
DIRECTORY=${TARGET}_recon
echo "creating directory of $DIRECTORY "
mkdir -p $DIRECTORY

case $2 in
	nmap-only)
		  nmap -sT $TARGET -F -T4 > $DIRECTORY/nmap.txt
	   	  echo "The result of nmap in $DIRECTORY/nmap.txt "
 	          echo "--------------------nmap------------------"
		  cat $DIRECTORY/nmap.txt
		  ;;
	gobuster-only)
		  gobuster dir --url $TARGET --wordlist /usr/share/wordlists/dirb/small.txt > $DIRECTORY/gobuster.txt
		  echo "The result of gobuster in $DIRECTORY/gobuster.txt" 
                  echo "--------------------gobuster------------------"
                  cat $DIRECTORY/gobuster.txt
		  ;;
	eyewitness-only)
		  eyewitness --web -f listdirectory.txt --timeout 3 -d $DIRECTORY/eyewitness --no-prompt
		  echo "The result of eyewitness in $DIRECTORY/eyewitness"
                  echo "--------------------eyewitness------------------"
		  ;;
	*)
		  nmap -sT $TARGET -F -T4 > $DIRECTORY/nmap.txt
                  echo "The result of nmap in $DIRECTORY/nmap.txt" 
                  echo "--------------------nmap------------------"
                  cat $DIRECTORY/nmap.txt

		  gobuster dir --url $TARGET --wordlist /usr/share/wordlists/dirb/small.txt > $DIRECTORY/gobuster.txt
                  echo "The result of gobuster in $DIRECTORY/gobuster.txt" 
                  echo "--------------------gobuster------------------"
                  cat $DIRECTORY/gobuster.txt

		  eyewitness --web -f listdirectory.txt --timeout 3 -d $DIRECTORY/eyewitness --no-prompt
                  echo "The result of eyewitness in $DIRECTORY/eyewitness"
                  echo "--------------------eyewitness------------------"
		  ;;
esac

