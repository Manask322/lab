#!/bin/bash
for i in `ls`
do
	if test -r $i
	then 
	if test -w $i
	then echo $i
    fi
	fi
done