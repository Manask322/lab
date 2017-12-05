#!/bin/bash
rm database.txt
select op in adding deletion finding displaying quit
do
	case $op in
		adding)echo "Enter name"
				read name
				echo "Enter rollno."
				read rollno
				echo "Enter semester"
				read sem
				echo "Enter three marks"
				read mark1
				read mark2
				read mark3
				echo "$name|$rollno|$sem|$mark1|$mark2|$mark3"|cat >> database.txt;;
		deletion)echo "Enter the name of the student you want to delete"
				read name
				echo "record:"
				grep -v "$name" database.txt | tee database.txt;;
		finding) echo "Enter name"
				 read name
				 grep "$name" database.txt;;
		displaying)cat database.txt;;
		quit) exit;;
	esac
done
