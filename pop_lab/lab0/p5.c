#include<stdio.h>
#include<string.h>
int main()
{
char s1[20],s2[34];
scanf("%s %s",s1,s2);
char cs[45];
for(int i=0;s1[i]!='/0';i++)cs[i]=s1[i];
int l=strlen(s1);
printf("length of %s: %d\n",s1,l);
strcat(s1,s2);
printf("%s after concatanation with %s:%s\n",cs,s2,s1);
char s3[34],s4[45];
scanf("%s %s",s3,s4);
strcpy(s3,s4);
printf("s3 after its string is copied from s4:%s",s3);
printf("\nenter a substring present in %s: ",s2);char ss[34];scanf("%s",ss);
char *i=strstr(s2,ss);
if(i==NULL)printf("substring not present");
else printf("substring present");
printf("\nenter two strings to compare:\n");char cs1[43],cs2[45];
scanf("%s %s",cs1,cs2);
if(!strcmp(cs1,cs2))printf("the strings are the same");
else printf("the strings are different");

}
