#include<stdio.h>
#include<math.h>
#define max 64
#define parent(i)((i-1)/2)
#define riight(i)(2*i)
#define left(i)(2*i+1)
#define start(l)(pow(2,l-1)-1)
#define end(l)(pow(2,l)-2)
#define level(p)((int)(log(max/p)/log(2)+1))
#define max_height 5
#define value(l) ((int)(max/(int)pow(2,l-1)))
#define neighbour(i)( i%2==0? i-1:i+1)
int memory[16];
void delete(int p_id)
{   
    // for(int k=0;k<16;k++)printf("%d\n",memory[k]);
    
    int temp,neigh;
    for(int i=0;i<16;i++){if(memory[i]==p_id){temp=i;break;}}

    // printf("@@@@@@%d",temp);
    neigh=neighbour(temp);
    if(memory[neigh]>0)memory[temp]=-1;
    else
    {  int par=temp;
        // printf("hi");
        while(par>0)
        {   
            if(memory[neighbour(par)]==-1)
            {   
                memory[par]=memory[neighbour(par)]=-3;
                memory[parent(par)]=-1;
            }
            else{
                // printf("%d %%%%",par);
                break;
            }
            par=parent(par);
        }
    }
    // printf("^^^^^\n");
    // for(int k=0;k<16;k++)printf("%d\n",memory[k]);
    
}
void alloc(int process,int p_id)
{
    int l=level(process);
    int s=(int)start(l);
    int e=(int)end(l);
    // printf("%d %d\n",s,e);
    int index=-1;
    for(int j=s;j<=e;j++)
    {
        if(memory[j]==-1){
            memory[j]=p_id;
            index=j;
            break;
        }
        if(memory[j]==-3)
        {   int flag=-1;
            int par=parent(j);
            while(par>0)
            {
                if(memory[par]>0)
                flag=1;
                break;
            }
            if(flag==1){continue;}
            else {index=j;memory[index]=p_id;
            if(memory[neighbour(index)]==-3)
            {       
                    memory[neighbour(index)]=-1;
                    // printf("---%d",memory[neighbour(index)]);
            }
            
            }
            break;
        }
    }
    if(index){
        int p=parent(index); 
        while(p>0){
            // printf("%d ",p);
            memory[p]=-2;//divide
            p=parent(p);
        }memory[p]=-2;
    }else{
        printf("memmoryfull\n");
    }
    // for(int k=0;k<16;k++)printf("%d\n",memory[k]);
}
void display()
{   
    for(int i=0;i<16;i++)
    {  int l=(int)(log(i+1)/log(2))+1;
        if(memory[i]==-1)
        printf("%d is free\n",value(l));
        if(memory[i]>0)
        {   
            printf("%d is occupied for space in block of %d bytes\n",memory[i],value(l));
        }
    }
}
void main()
{   memory[0]=-1;//free
    for(int i=1;i<16;i++)memory[i]=-3;//non-existent    
    // alloc(14,1);
    alloc(7,1);
    alloc(15,2);
    alloc(31,3);
    // alloc();
    // alloc();
    display();
    delete(1);
    // printf("sdcsdc");
    display();
}