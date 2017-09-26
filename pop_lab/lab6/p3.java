class p
{   int a,b;
	p(int a,int b)
	{
   this.a=a;this.b=b;
	}
	void swap(int a,int b)
	{
		int t;
		t=a;a=b;b=t;
	}
	void swap1(p obj)
	{
		int t;
		t=obj.a;obj.a=b;obj.b=t;
	}
}
class p3
{
	public static void main(String[] args)
	{   
		int x=3,y=4;
		p pobj=new p(x,y);
		System.out.println("before swapping x: "+x+" y: "+y);
		pobj.swap(x,y);
		System.out.println("After swapping by call by value x: "+x+" y: "+y);
		System.out.println("before swapping a: "+pobj.a+" b: "+pobj.b);
		pobj.swap1(pobj);
        System.out.println("after swapping by call by reference a: "+pobj.a+" b: "+pobj.b);
	}
}