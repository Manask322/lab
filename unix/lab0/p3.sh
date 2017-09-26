#!/bin/bash
osch=0
echo -e "1.Sun OS \n 2.Red Hat\n"
read osch
if [ $osch -eq 1 ];
then 
echo "you chose Sun OS"
else
if [ $osch -eq 2 ];
then
echo "you chose Red Hat"
else
echo "choose 1 or 2"
fi
fi
