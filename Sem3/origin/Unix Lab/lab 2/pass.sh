#!/bin/bash
echo Enter password
stty -echo 
read p
stty echo
printf "The password is $p\n"
