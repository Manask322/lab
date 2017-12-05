#!/bin/bash
c1=0
c2=0
for i in `ls`
do
	if test -f $i 
	then((c1=c1+1))
	fi
	if test -d $i
	then ((c2=c2+1))
    fi
done
echo " $c1 $c2 "
