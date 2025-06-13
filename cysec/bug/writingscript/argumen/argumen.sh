#!/bin/bash

nmap -sT $1 -p 80 -T4
dirsearch -u $1 -e php
