import mypack.*
class p3a
{
	public void main(String args[])
	{
		p3 obj = new p3();
		p3.message();
		p3b obj2 = new p3b()
		obj2.message2();
	}
}
class p3b{
	public void message2(String args[])
	{
		System.out.println("this from an external class");
	}
}