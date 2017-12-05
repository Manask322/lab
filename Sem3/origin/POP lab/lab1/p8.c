#include<stdio.h>
#include<stdlib.h>
struct student
{
int n;
char name[67];
};
int main()
{int n;
printf("Enter no. of students");
scanf("%d",&n);
struct student *s;
s=(struct student*)malloc(sizeof(struct student *)*n);
printf("\nEnter details\n");
for(int i=0;i<n;i++)
scanf("%d %s",&(s+i)->n,(s+i)->name);
printf("\n Details:\n");
for(int i=0;i<n;i++)
printf("%d %s\n",(s+i)->n,(s+i)->name);
}
