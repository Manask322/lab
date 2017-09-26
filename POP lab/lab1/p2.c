#include<stdio.h>
#include<string.h>
struct prod
{
char name[67];
int up;
};
int market(struct prod *p[],char pname[],int quantity)
{int q,i;
for(i=0;i<3;i++)
{

if(!strcmp(pname,(p+i)->name))q=(p+i)->up;
printf("total cost: %d",q*quantity);
}


}
int main()
{int i;
struct prod *p[3];
printf("Enter name,quantity");
for(i=0;i<3;i++)
scanf("%s %d",(p+i)->name,&(p+i)->up);
//strcpy(p[0]->name,"pen");strcpy(p[1]->name,"calculator");strcpy(p[2]->name,"pouch");
//p[0]->up=10;p[1]->up=90;p[2]->up=30;
char pname[67];int quantity;scanf("%s %d",pname,&quantity);
market(p,pname,quantity);
}
