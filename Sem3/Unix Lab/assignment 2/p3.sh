#!/bin/bash
min=5600
max=0
i=0
max_c=0
min_c=0
read -a arr
for i in "${arr[@]}"
do
	count=0
    if [ $i -gt $max ]
    then
    max=$i
    fi
    if [ $i -lt $min ]
    then
    min=$i
    fi 
    for j in "${arr[@]}"
    do
    	if [ $i -eq $j ]
    	then ((count=count+1))
        fi
    done
    echo "$i element repeats $count times"
done

echo "max is $max min is $min" 
