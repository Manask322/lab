#!/bin/bash
echo "number of rows first matrix"
read r1
echo "number of columns first matrix"
read c1
declare -A a
echo "Enter first matrix"
for((i=0;i<r1;i++))
do
	for((j=0;j<c1;j++))
	do
		read t
		((a[$i,$j]=$t))
		#echo ${a[$i,$j]}
	done
done
#echo ${a[*]}
echo "number of rows second matrix"
read r2
echo "number of columns second matrix"
read c2
if [ $r1 -ne $r2 ]
then echo "row1 should be equal to row 2";exit
fi
if [ $c1 -ne $c2 ]
then echo "column1 should be equal to column2";exit
fi
declare -A b
echo "Enter second matrix"
for((i=0;i<r2;i++))
do
	for((j=0;j<c2;j++))
	do
		read t
		((b[$i,$j]=$t))
	done
done
declare -A c
for((i=0;i<r2;i++))
do
	for((j=0;j<c2;j++))
	do
		((c[$i,$j] = ${a[$i,$j]}+${b[$i,$j]}))
	done
done
for((i=0;i<r2;i++))
do
	for((j=0;j<c2;j++))
	do
		echo -n "${c[$i,$j]} "
	done
    echo ""
done 