interface stack
{   
    int pop();
	void insert(int k);
	int  peek();
	void display();
	boolean isEmpty();
	boolean isFull();
}
class stackADT implements stack
{
  int top=-1;
  int[] elements=new int[45]; 	
  public void insert(int k)
  {
     if(this.isFull())
     {
     	System.out.println("stack full");
     }
     else
     {
     	this.top+=1;
     	this.elements[this.top]=k;
     }
  }
  public int pop()
  {
  	if(this.isEmpty())
  	{
  		System.out.println("stack empty");
  	}
  	else{
  		int x=this.elements[this.top];
  		this.top-=1;
  		return x;
  	   }
  	  return -1;
  }
  public int peek()
  {
  	return this.elements[this.top];

  }
  public void display()
  {
  	int i=0;
  	while(i<=this.top)
  	{
  		System.out.print(this.elements[i]);
  		i++;
  	}

  }
  public boolean isEmpty()
  {
  	if(this.top==-1)return true;
  	else return false;
  }
  public boolean isFull()
  {
  	if(this.top==44)return true;
  	else return false;
  }
}
class p7
{
	public static void main(String[] args)
	{
		stackADT s=new stackADT();
		s.insert(4);
		System.out.println("***");
		s.display();
		s.insert(6);
		System.out.println("***");
		s.display();
		System.out.println("***");
		System.out.println(s.pop());
		System.out.println("***");
		s.display();
		System.out.println(s.peek());
	}
}