#!/bin/bash
echo "Enter your unix marks"
read u
echo "Enter your java marks"
read j
echo "Enter your DS marks"
read d
a=$(echo "scale=0;($u+$j+$d)/3"|bc)
#a=$(python -c "print $total/3")
echo $a
if [ $a -ge 70 ]
then
echo "Distinction"
exit
fi
if [ $a -ge 60 ]
then 
echo "First Class"
exit
fi
if [ $a -ge 50 ]
then
echo "Second Class"
exit
fi
if [ $a -ge 40 ]
then
echo "Third Class"
exit
fi
if [ $a -lt 40 ]
then
echo "Fail!!!"
exit
fi
#- is 70 or above "Distinction"
#- is 60 <= 70 "First Class"
#- is 50 <= 60 "Second Class"
#- is 40 <= 50 "Third Class"
#- otherwise "Fail"
