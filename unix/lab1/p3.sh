#!/bin/bash
echo -n "enter the number of elements"
read n
m=`expr $n`
echo "enter the elements"
sum=0
while [ $m -gt 0 ]
do
read a
sum=`expr $sum + $a`
m=`expr $m - 1`
done
echo "average is :"
echo "scale=2;`expr $sum/$n`"|bc

