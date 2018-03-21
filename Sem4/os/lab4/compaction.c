#include<stdio.h>
#include<stdlib.h>
struct Node{
    int id;
    int memory;
    int start;
    int end;
    int flag;
    struct Node* next;
};
struct Node * createnode(int id,int memory){
    struct Node* node=(struct Node*)malloc(sizeof(struct Node));
    node->id=id;
    node->memory=memory;
    node->next=NULL;
    node->flag=1;
    return node;
}
void insert(struct Node* head,int id,int memory){
    if(head->memory>memory){
        struct Node* node=createnode(id,memory);
        struct Node *temp;//insert AT HEAD
        temp=head->next;
        head->next=node;
        node->next=temp;
        //memory and start end
        head->memory=head->memory-memory;
        head->end=head->end-memory;
        int prev=head->end;
        while(node!=NULL){
            node->start=prev+1;
            node->end=prev+1+node->memory;
            prev=node->end;
            node=node->next;
        }
    }else{
        printf("memory full");
    }
}

void display(struct Node* head){
    struct Node* node=head;
    while(node!=NULL){
        if(node->flag==1)
        printf("process id :%d start:%d end:%d memory:%d\n",node->id,node->start,node->end,node->memory);
        else
        printf("process id :%d start:%d end:%d free memory:%d\n",node->id,node->start,node->end,node->memory);
        node=node->next;
    }
}
void delete(struct Node * head,int id){
    struct Node* node=head;
    while(node!=NULL){
        if(node->id==id){
            node->flag=0;
            printf("ddcdc");
        }
        node=node->next;
    }
}
void compact(struct Node * head){
    struct Node* node=head->next;
    struct Node * prev_n=head;
    int freemem=0;
    while(node!=NULL){
        if(node->flag==0){
            freemem=freemem+node->memory;
            prev_n->next=prev_n->next->next;
        }
        prev_n=node;
        node=node->next;
    }
    //update index
    head->memory+=freemem;
    head->end=head->memory+1;
    int prev=head->end;
    node=head->next;
    while(node!=NULL){
        node->start=prev+1;
        node->end=prev+1+node->memory;
        prev=node->end;
        node=node->next;
    }
}
void main(){
    int memory=2000;
    struct Node head;
    head.memory=memory;
    head.start=1;
    head.end=memory;
    head.next=NULL;head.flag=0;
    insert(&head,1,300);
    insert(&head,2,250);
    // display(&head);
    delete(&head,1);
    // display(&head);
    compact(&head);
    display(&head);
}