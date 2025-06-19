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
	echo "this scan was created $today"
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

echo "generating report"
echo "this scan was created $today" > $directory/report

echo "the report of nmap scan in $directory/report"
grep -E "^\S+\s+\S+\s+\S+$" $directory/nmap.txt >> $directory/report	#we use -E so grep know we use regex and \s mean match any whitespaces \S match any non whitespaces in this case [PORT STATE SERVICE]
# * match preceeding zero or more times					# ^ match start of the string in line. where $ match end string in line
# + match preceeding character one or more times			# \ escape special character. \w match any character. \d match any digit
# {3} match the preeceeding character 3 time
# {1, 3} match the preeceeding character 1 or 3 time
# {1, } match the preeceeding character 1 or 3 time			# . match with any single character 
# [abc] match one of the character within bracket
# [a-z] match one of the character within the range a to z bracket
# (a|b|c) match a or b or c

echo "the report of gobuster scan in $directory/report"
cat $directory/gobuster.txt >> $directory/report
