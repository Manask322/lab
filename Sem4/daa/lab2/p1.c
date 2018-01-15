#include<stdio.h>
#include<stdlib.h>
void solvehanoi(int n,char s,char i,char t)
{
  if(n>=1)
  {
  	solvehanoi(n-1,'S','T','I');
  	printf("move disk %d from %c to %c \n",n,s,t);
  	solvehanoi(n-1,'I','S','T');
  }
}
int main()
{
	int n;
	scanf("%d",&n);
	solvehanoi(n,'S','I','T');
}