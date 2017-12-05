#!/bin/bash
for((i=1;i<=4;i++))
do
	for((j=i;j<=2*i-1;j++))
	do
		echo -n $j
	done
	for((j=2*i-2;j>=i;j--))
	do
		echo -n $j
	done
	echo ""
done
