#!/bin/bash
if [ -z $1 ];
then
rental="unknown"
elif [ -n $1 ];
then
rental=$1
fi
case $rental in 
"car") echo "u rented $rental";;
"bus") echo "u rented a $rental";;
"bike") echo "u rented a $rental";;
*) echo "u didnt rent $rental";;
esac

