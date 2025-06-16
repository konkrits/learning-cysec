#!/bin/bash

nmap -sT 10.0.2.5 -p 3306  >>/dev/null -oG mysql

cat mysql | grep open > mysql2

cat mysql2
