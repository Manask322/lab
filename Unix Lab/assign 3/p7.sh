#!/bin/bash
echo "enter the string"
read  s
len=`echo ${#s}`
while [ $len -ne 0 ]
do
	re=$re`echo $s|cut -c $len`
	((len=len-1))
done
echo $re
for i in "${a[@]}"
do
	echo $i
done
if test "$re" == "$s" 
then
echo "Palindrome"
else
echo "Not a PAlindrome"
fi