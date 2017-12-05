import java.util.Scanner;
class area
{
	public void compute(int r,int h)
	{ 
         System.out.println("The volume is "+(3.14*r*r*h/3));
	}
	public void compute(int l,int b,int h)
	{
		System.out.println("The volume is "+(l*b*h));
	}
	public void compute(int r)
	{
		System.out.println("The volume is "+(2*3.14*r*r));
	}
	public void py_compute(int l,int w,int h)
	{
		System.out.println("The volume is "+(Math.sqrt(h*h+l*l/ 4)*10));
	}
}
class p5
{
	public static void main(String args[])
	{
		Scanner input = new Scanner(System.in);
        System.out.println("enter dimensions of cone");
        int r=input.nextInt();
        int h= input.nextInt();
        area cone = new area();
        cone.compute(r,h);
        System.out.println("enter dimensions of rectangular prism");
        int l=input.nextInt();
        int b=input.nextInt();
        h=input.nextInt();
        area rprism = new area();
        rprism.compute(l,b,h);
        System.out.println("enter dimensions of pyramid");
         l=input.nextInt();
        int w=input.nextInt();
        h=input.nextInt();
        area pyramid = new area();
        pyramid.py_compute(l,w,h);
        System.out.println("enter dimensions of hemesphere");
        r=input.nextInt();
        area hem =new area();
        hem.compute(r);
	}
}