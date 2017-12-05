#!/bin/bash 
echo "Enter text"
cat > t.txt
sed '1i\
<html>
' text > temp.txt      
sed '$a\
</html>
' temp.txt | tee t.txt 
rm temp.txt             
rm ex.txt
rm ex1.txt
echo "Enter text"
cat > ex.txt
sed '1,3s/|/:/g' ex.txt > ex1.txt
echo ""
echo ""
cat ex1.txt