#!/bin/bash
echo $$
sort text > text1 &  
ps
l=$(ps | wc -l) 
((l-=1))
echo $l