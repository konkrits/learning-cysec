#!/bin/bash

nmap -sT 192.168.72.129 -p 80
dirsearch -u http://192.168.72.129 -e php


#selamat kamu menulis bash script!!!
#tapi ini ga terlalu berguna
