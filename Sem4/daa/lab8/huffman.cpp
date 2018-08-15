#include<bits/stdc++.h>
using namespace std;
string encode;
class Node
{
    public:
    Node *left;
    Node *right;
    Node* parent;
    int freq;
    char c;
    Node(Node* left,Node* right,int freq,char c)
    {
        this->left=left;
        this->right=right;
        this->freq=freq;
        this->c=c;
    }
};
vector<int> frequency;
vector<char> symbols;
struct comparator {
 bool operator()(Node& i,Node& j) {
 return i.freq > j.freq;
 }
};  
Node huffman(vector<int>freqency,vector<char>symbols)
{
    vector<Node> leaves;
  for(int i=0;i<symbols.size();i++)
    {
        leaves.push_back(Node(nullptr,nullptr,frequency[i],symbols[i]));
    }
    priority_queue< Node,vector<Node>,comparator> minHeap;
    for(int i=0;i<leaves.size();i++)
    {
        minHeap.push(leaves[i]);
    }
    while(minHeap.size()==1)
    {
         Node t1=minHeap.top();
        minHeap.pop();
         Node t2=minHeap.top();
         minHeap.pop();
        Node parent(&t1,&t2,t1.freq+t2.freq,'-1');
        t1.parent=&parent;
        t2.parent=&parent;
        minHeap.push(parent);
    }
    // for(int i=0;i<leaves.size();i++)
    // {
    //     printf("charecter %c:",leaves[i].c);
    //     Node* parent=leaves[i].parent;
    //     if(parent==NULL)
    //     {
    //         printf("null ");
    //     }
    //     while(parent!=NULL)
    //     {
    //         if(parent->left->c==leaves[i].c)
    //         {
    //             printf("0");
    //         }
    //         else printf("1");
    //        parent=parent->parent;
    //     }
    //     printf("\n");
    // }

    return minHeap.top();
}
void display(Node* tree)
{   
    if(&tree==nullptr)
    {
        printf("Char : %c %s",tree->c,encode);
        return;
    }
    encode.push_back('0');
    display(tree->left);
    encode.pop_back();
    encode.push_back('1');
    display(tree->right);
    encode.pop_back();
}
int main()
{
    int n=4;
    frequency={1,9,4,5};
    symbols={'a','b','c','d'};
    Node tree=huffman(frequency,symbols);
    display(&tree);
}
