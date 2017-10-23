#!/bin/bash
hour=$(date +"%H")
min=$(date +"%M")
if [ $hour -le 11 ]
	then
	echo "good morning"
	exit	 
fi
if [ $hour -le 17 ]
	then
	echo "good Afternoon"
    exit
fi
if [ $hour -le 19 ]
	then
	echo "good Evening"
	exit
fi
echo "good night"