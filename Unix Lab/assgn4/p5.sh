#!/bin/bash 
cat > t.txt
sed '1i\
<html>
' t.txt > temp.txt
sed '$a\
</html>
' temp.txt | tee t.txt 
rm temp.txt
cat > ex.txt
sed '1,3s/|/:/g' > ex.txt