#!/bin/bash

today=$(date)									#we made our command become variable just keep in mind that for the syntax VARIABLE=$(command)	
target=$1									#in bash $1 refers for argument 1 and $2 is so on
directory=$target								#bash for variable is variable=value

echo "making directory of $target"						#for the echo command you should give him scape
mkdir -p $directory

nmap_scan()									#for making function the syntax is function_name()
{								   			#use curly bracket 	   {
	nmap -sT $target -F -T4 > $directory/nmap.txt					#			   }
	cat $directory/nmap.txt
	echo "---------------nmap-----------------"
	echo "the result of nmap scan in $directory/nmap.txt"
}
gobuster_scan()
{
	gobuster dir --url $target --wordlist /usr/share/wordlists/dirb/small.txt > $directory/gobuster.txt
	cat $directory/gobuster.txt
	echo "---------------------gobuster---------------"
	echo "the result of gobuster scan in $directory/gobuster.txt"
}
eyewitness_scan()
{
	eyewitness --web -f listdirectory.txt --timeout 4 --no-prompt -d $directory/eyewitness
        echo "-------------------eyewitness---------------"
        echo "the result of gobuster scan in $directory/eyewitness"
}

case $2 in								 #the case syntax is ( case $variable in )

	nmap-only)							 #	case1)
		nmap_scan						 #		do something
		;;
	gobuster-only)
		gobuster_scan
		;;
	eyewitness-only)
		eyewitness_scan
		;;
	*)								#* means execute command if you don't give argument
		nmap_scan
		gobuster_scan
		eyewitness_scan
		;;
esac									#for end of case use ( esac )
