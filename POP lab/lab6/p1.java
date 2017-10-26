class p1
{
	public static void main(String[] args)
	{   int a=0,b=9,c=0;
		int[] arr=new int[4];
		try
		{
		    if(args.length>0)c=b/a;
		    else arr[5]=3;
        }
        catch(ArithmeticException e)
        {   e.printStackTrace();
           System.out.println(e.getMessage());
        	System.out.println("Dont divide by zero");
        }
        catch(ArrayIndexOutOfBoundsException e)
        {   System.out.println(e.getMessage());
        	e.printStackTrace();
        	System.out.println("index out of bounds");
        }
	}
}