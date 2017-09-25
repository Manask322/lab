#include<stdio.h>
int main()
{int f[89]={0};
char s[56],c;
printf("\nEnter the string,charecter to be searched\n");
//scanf("%[^\n]s",s);
gets(s);
scanf("%c",&c);
int t=0;
for(int i=0;s[i]!='\0';i++)
{
if(s[i]==c)
{t++;if(t==1)printf("Position(s):\n");
printf("%d ,",i+1);
f[s[i]-'a']++;
}
}
if(t==0)printf("\nCharecter not found");
else printf("\nnumber of repetiton:%d",f[c-'a']);
}
