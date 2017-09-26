#!/bin/bash
if test $1 -gt 0
then 
echo "$1 is positive"
elif test $1 ieq 0
then
echo "$1 is zero"
else
echo "$1 is negative"
fi
