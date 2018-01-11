#include<stdio.h>
#include<stdlib.h>
struct node 
{
  int data;
  struct node* next;
};
struct node* newNode(int key)
{
	struct node* temp=(struct node*)malloc(sizeof(struct node));
	temp->data=key;temp->next=NULL;
}
void main()
{
	// int *a;
	// // int b;
	// a=(int*)malloc(44*sizeof(int));
	// printf("%p to %p",a,a+sizeof(a));
	// // printf("%ld",sizeof(a));
	// free(a);
 //    #define K (1024)
 //         char *p1,*p2;
 //         p1 = (char *)malloc(3*K);
 //          p2 = (char *)malloc(4*K);
 //         free(p1);
 //          p1 = (char *)malloc(4*K);
 //         if(p1==NULL)printf("Null alloc");  
	struct node* node1=newNode(0);
	struct node* node2=newNode(1);
	struct node* node3=newNode(2);
	struct node* node4=newNode(3);
	struct node* node5=newNode(4);
 //    printf("%d \n",node1);
 //    printf("%ld \n",sizeof(node1));
 //    printf("%d \n",node2);
 //    printf("%ld",sizeof(node2));
    struct node* block[6]; 
     block[0]=node1;
     block[1]=node2;
     block[2]=node3;
     int i;
     // for(i=0;i<=2;i++)
     // 	// printf("%d\n",block[i]);
     free(node1);
     printf("%d\n", node1);
     // for(i=0;i<=2;i++)
     // 	// printf("%d\n",block[i]);
}