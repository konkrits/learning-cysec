#!/bin/bash 

nmap -sT 192.168.1.11 -p 3306 >/dev/null -oG task22

cat task22 | grep open > taask2

cat taask2
