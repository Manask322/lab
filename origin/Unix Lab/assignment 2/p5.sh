#!/bin/bash
n=1
while [ $n -lt 1000 ]
do
ans=0
num=$n
    while [ $num -ne 0 ]
    do
    	((b=num%10))
	    ((ans=ans+b*b*b))
	    ((num=num/10))
    done
    if [ $ans -eq $n ]
    then echo $n
    fi
((n=n+1))
done