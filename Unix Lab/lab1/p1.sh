#!/bin/bash
echo "Enter Amount:"
read p
echo "Enter Time:"
read t
echo "Enter ROI:"
read r
 
((i=$p*$t*$r))
#i=` expr $i / 100 `
 echo -n "Simple Interest: "
echo "scale=2;`expr $i/100`"|bc
echo "enter radius"
read ra
area=` expr 22 \* $ra \* $ra`
#area=` expr $area / 7`
#echo "scale=4; `expr $area / 7` " | bc
echo "scale=2; `expr $area/7`"|bc

