#!/bin/bash
echo "Enter file1"
read f1
echo "Enter file2"
read f2
if test -f $f1
then
if test -f $f2
then cat $f1|cat >> $f2
fi
fi