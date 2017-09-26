import java.util.Scanner;
class square
{   int a;
	square()
    {
    	a=-1;
    }
    square(int a)
    {
    	this.a=a;
    }
    void area()
    {
    	if(this.a!=-1)System.out.println((this.a*this.a));
    	else System.out.println("value not passed");
    }
}
class rectangle
{
int l,b;
rectangle()
{
	l=-1;
	b=-1;
}
rectangle(int l,int b)
{
	this.l=l;
	this.b=b;
}
void area()
{
	if(this.l!=-1)System.out.println((this.l*this.b));
    	else System.out.println("value not passed");
}
}
class cube
{
	int a;
	cube()
	{
		a=-1;
	}
	cube(int a)
	{
		this.a=a;
	}
	void area()
	{
		if(this.a!=-1)System.out.println((this.a*this.a*6));
    	else System.out.println("value not passed");
	}
}
class sphere
{
	int r;
	sphere()
	{
		r=-1;
	}
	sphere(int r)
	{
		this.r=r;
	}
	void area()
	{
		if(this.r!=-1)System.out.println((this.r*this.r*4*3.14));
    	else System.out.println("value not passed");
	}
}
class p6
{
	public static void main(String args[])
	{
		square square1= new square();
		square1.area();
		square square2= new square(3);
		square2.area();
		rectangle rectangle1= new rectangle();
		rectangle1.area();
		rectangle rectangle2= new rectangle(3,4);
		rectangle2.area();
		cube cube1= new cube();
		cube1.area();
		cube cube2= new cube(3);
		cube2.area();
		sphere sphere1= new sphere();
		sphere1.area();
		sphere sphere2= new sphere(3);
		sphere2.area();
	}
}