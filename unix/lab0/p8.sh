#!/bin/bash
i=1
while [ $i -le 10 ]
do 
echo -e "$1*$i=`expr $1\*$i`\n"
i=`expr $i + 1`
done
