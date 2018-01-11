#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void main(){
	void *a;
	a=malloc(sizeof(sizeof(int)*4));
	memset(a,0,sizeof(int));
	memset(a+2*sizeof(int),1,sizeof(int));
    memset(a+sizeof(int),'a',sizeof(char));    
}