#!/bin/bash
n=1
while [ $n -lt 10 ]
do
	echo $n
	n=`expr $n + 1`
done