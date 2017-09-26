#!/bin/bash
i=0
read -a a
c=0
cn=0
cz=0
for i in "${a[@]}"
do
	if [ $i -gt 0 ] 
	then ((c=c+1))
    fi
    if [ $i -eq 0 ]
    then ((cz=cz+1))
    fi
    if [ $i -lt 0 ]
    then ((cn=cn+1))
    fi
done
echo "pos:$c neg:$cn zeros:$cz"
for ((i=0;i<9;i++))
do
 for((j=0;j<9;j++))
 do
if [ ${a[j]} -ge ${a[$((j+1))]} ]
then
  v=${a[$j]}
  a[$j]=${a[$((j+1))]}
  a[$((j+1))]=$v
    fi
 done
done
echo ${a[*]}