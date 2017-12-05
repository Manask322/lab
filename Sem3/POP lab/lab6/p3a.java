import mypack.*;
class p3a
{
	public static void main(String args[])
	{
		mypack.p3 obj = new mypack.p3();
		obj.message();
		p3b obj2 = new p3b();
		obj2.message2();
	}
}
class p3b{
	public void message2()
	{
		System.out.println("this from an external class");
	}
}