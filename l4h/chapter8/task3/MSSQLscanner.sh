#!/bin/bash

echo "enter the first ip octet: "
read fip

echo "enter the last ip octet: "
read lip

echo "enter the port number: "
read nport

sudo nmap -sT $fip/$lip -p $nport > /dev/null -oG mssqlscan

cat mssqlscan | grep open > mssqlscan2

cat mssqlscan
