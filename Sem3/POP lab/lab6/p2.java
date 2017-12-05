class p2
{
	public static void main(String[] args)
	{ int a=0,b=90,c=0;
	  int[] arr=new int[6];
	  try{
	  try
	  {
           c=b/a;
	  }
	  catch(ArithmeticException e)
	  { 
	  	e.printStackTrace();
	  	arr[7]=3;	
	  }
	}
	catch(ArrayIndexOutOfBoundsException e)
	{
		e.printStackTrace();
	}

   }
}