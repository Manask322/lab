import java.util.Scanner;
class p
{
	class p1
	{
		void add(int a,int b)
		{
			int ans=a+b;
			System.out.println(ans);
		}
	}
}
class p2
{
	static class p3
    {
    	void add(int a,int b)
    	{
    		System.out.println((a+b));
    	}
    }
}
class p5
{
	public static void main(String args[])
	{
		p pobj = new p();
		p.p1 p1obj = pobj.new p1();
		p1obj.add(2,3);
		p2.p3 p3obj = new p2.p3();
		p3obj.add(5,6);
	}
}