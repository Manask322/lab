#!/bin/bash
select k in month year quit
do
	case $k in
		month)m=`date +%m`
           echo $m;;
        year)yr=`date +%Y`
            echo $yr;;
        quit)echo bye bye
            exit;;
        *)
    esac
done