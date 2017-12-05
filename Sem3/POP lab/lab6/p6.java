class myexception extends Exception
{
	myexception(String str)
	{
		super(str);
	}
}
class p6
{
	public static void main(String[] args)
	{
		try
		{
			throw new myexception("My own exception");
		}
		catch(myexception e)
		{
			e.printStackTrace();
		}
	}
}