#include<stdio.h>
#include<stdlib.h>
struct node
{
	int key;
	struct node* left;
	struct node* right;

};
struct node * newNode(int item)
{
	struct node* temp=(struct node*)malloc(sizeof(struct node));
	temp->key=item;
	temp->left=temp->right=NULL;
	return temp;
}
void inorder(struct node* root)
{

	if (root!=NULL)
	{
		inorder(root->left);
		printf("%d ",root->key);
		inorder(root->right);		
	}
}
void insert(struct node* root,int key)
{
	if(root==NULL)root=newNode(key);
	struct node* temp=root;
	struct node* p=temp;
	while(temp!=NULL)
	{    p=temp;
         if(key<temp->key)temp=temp->left;
         else temp=temp->right;
	}
	printf("%d ", p->key);
    if(key<p->key)p->left=newNode(key);
    else p->right=newNode(key);
    // printf("%d ", root->key);
}
int main()
{
	struct node* root =NULL;
	insert(root, 30);
 
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    inorder(root);
    return 0;
}