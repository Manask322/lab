#!/bin/bash
echo "Enter name"
read name
echo "Enter adress"
read adress
echo "$name|$adress" | cat >> adress.lst 