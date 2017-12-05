s1=input("1:")
s2=input("2:")
s3=input("3:")

len1=len(s1)
len2=len(s2)
len3=len(s3)
s4=""
i=0
while i<len1:
    if s1[i:i+len2]==s2:
        s4=s4+s3
        i=i+len2
        if i>len1:
            break
    else:
            s4=s4+s1[i]
            i=i+1
print(s4)