#!/bin/bash
echo "Enter two numbers:"
read a
read b
echo "Enter the operand:"
read o
echo -n "Answer is :"
case $o in
"*") echo "scale=2;`expr $a \* $b`"|bc;;
"/") echo "scale=2;`expr $a/$b`"|bc;;
"+") echo "scale=2;`expr $a + $b`"|bc;;
"-") echo "scale=2;`expr $a - $b`"|bc;;
"%")echo "scale=0;`expr $a % $b`"|bc;;
*)echo "Invalid operand";;
esac
