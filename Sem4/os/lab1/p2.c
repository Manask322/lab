#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void main(){
	void *a;
	int memory;
	a=malloc(sizeof(sizeof(int)*4));
	while(1)
	{
		printf("Enter value you want to enter(press q to quit)");
        
	}
	memset(a,0,sizeof(int));
	memset(a+2*sizeof(int),-1,sizeof(int));
    memset(a+sizeof(int),'a',sizeof(char));   
    printf("%s\n", );
}