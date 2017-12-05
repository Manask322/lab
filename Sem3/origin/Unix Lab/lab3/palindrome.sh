#!/bin/bash
echo "enter the string"
read s
if test "$(echo $s|rev)" == "$s" 
then
echo "Palindrome"
else
echo "Not a Palindrome"
fi
