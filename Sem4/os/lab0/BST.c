#include<stdio.h>
#include<stdlib.h>
struct node
{
	int key;
	struct node* left;
	struct node* right;
	struct node* parent;

};
struct node * newNode(int item,struct node* parent)
{
	struct node* temp=(struct node*)malloc(sizeof(struct node));
	temp->key=item;
	temp->left=temp->right=NULL;
	temp->parent=parent;
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
struct node* maximum(struct node* n)
{
	if(n==NULL)return NULL;
	struct node* temp=n;
	struct node* p=NULL;
	while(temp!=NULL){
		p=temp;
		temp=temp->right;
	}
	return p;
}
struct node* insert(struct node* root, int data)
{
	struct node *curr = root;
	struct node *parent = NULL;
	if (root == NULL)
	{
		root = newNode(data,NULL);
		return root;
	}
	while (curr != NULL)
	{
	    
		parent = curr;
        if (data < curr->key)
			curr = curr->left;
		else
			curr = curr->right;
	}
	if (data < parent->key)
		parent->left = newNode(data,parent);
	else
		parent->right = newNode(data,parent);
	return root;
}
struct node* predecessor(struct node* n)
{   struct node* y=NULL;
	if(n==NULL)return NULL;
    else if(n->left!=NULL )return maximum(n->left);
	else{
		struct node* y=n->parent;
	    while(n->key=y->left->key  && y!=NULL)
		{
		    n=y;
			y=n->parent;
		}
	}
	return y;
}
void delete(struct node* n)
{
	if(n==NULL){return ;}
	else if(n->left==NULL && n->right==NULL) 
	{
         struct node* parent=n->parent;
		 if(n->key<parent->key)parent->left=NULL;
		 else parent->right=NULL;
		 return;
	}
	else if(n->left!=NULL && n->right!=NULL)
	{
         struct node* pred=predecessor(n);
		 n->key=pred->key;
		 delete(pred);
		 return;	
	}
	else{
		struct node* parent=n->parent;
		if(n->key<parent->key)
		{
			if(n->left!=NULL){parent->left=n->left;(n->left)->parent=parent;}
			else{parent->left=n->right;(n->right)->parent=parent;}
		}
		else
		{
			if(n->left!=NULL){parent->right=n->left;(n->left)->parent=parent;}
			else{parent->right=n->right;(n->right)->parent=parent;}
		}
	}
}
int main()
{
	struct node* root =NULL;
	root=insert(root, 30);
    root=insert(root, 20);
    root=insert(root, 40);
    root=insert(root, 70);
    root=insert(root, 60);
    root=insert(root, 80);
    inorder(root);
	delete(root);
	printf("sdfsdf");
	inorder(root);
    return 0;
}