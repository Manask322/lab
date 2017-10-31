#!/bin/bash
echo $$
sort text > text1 &  
l=$(ps | wc -l) 
((l-=1))
echo $l