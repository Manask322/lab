#!/bin/bash
select k in home name today terminal quit 
do
	case $k in 
		home)echo "$HOME";;
        name)who|cut -c 1-7 ;;
        today)date +"today is :%D"
              echo -n "The number of users:" ;users|wc -w;;
        terminal)echo -n "termional number:";tty|cut -c 10-;;
        quit)exit;;
        *)echo "Improper option";;
    esac
done
