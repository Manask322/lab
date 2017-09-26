#include<stdio.h>
struct student
{
int n;
char name[34];

};
int main()
{
int num;printf("number of students?");scanf("%d",&num);
struct student s[num];
printf("enter number followed by name");
for(int i=0;i<num;i++)scanf("%d %s",&s[i].n,s[i].name);
printf("\n student details\n");
for(int i=0;i<num;i++)printf("%d %s \n",s[i].n,s[i].name);
}
