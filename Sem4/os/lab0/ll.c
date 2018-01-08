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
    temp->data=key;
    temp->next=NULL;
    return temp;
}
struct node* insert(struct node* sent,int key,int pos)
{
    int i=0;
    struct node* temp=sent;
    while(i<pos)
    {
       i++;
       temp=temp->next;
    }
    temp->next=newNode(key);
    return sent;
}
void traverse(struct node* sent)
{
    struct node* temp=sent;
    while(temp!=NULL)
    {
        temp=temp->next;
        printf("%d ",temp->data);
    }
}
int main()
{   //sentinel node
    printf("hello");
    
    struct node* sent=(struct node*)malloc(sizeof(struct node));
    
    // sent->data=NULL;
    // sent->next=NULL;
    sent=insert(sent,5,0);
    traverse(sent);

    sent=insert(sent,66,0);
    traverse(sent);
    
    sent=insert(sent,2,0);
    traverse(sent); 
    
    sent=insert(sent,0,0);
    traverse(sent); 
    
    sent=insert(sent,5,0);
    traverse(sent);

    return 0;
}