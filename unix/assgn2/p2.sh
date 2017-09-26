#!/bin/bash
echo "Enter file/directory"
read a
if test -f $a
then cat $a
fi
if test -d $a
then cd $a;ls 
fi
