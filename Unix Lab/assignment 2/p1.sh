#!/bin/bash
a=$1
b=$2
while [[ ($a -le 0 )  || ( $b -le 0 ) ]]
do
	
	read a
	read b
done
c=$(echo "scale=2;`expr $a/$b`"|bc )
echo "division value $c "