import java.util.Scanner;
class p1
{
	public static void main(String args[])
	{
		Scanner input = new Scanner(System.in);
		System.out.println("Enter three numbers");
		int a=input.nextInt();
		int b=input.nextInt();
		int c=input.nextInt();
		if (a<=b && b<=c)
		{
			System.out.println("Increasing order");
		}
		else if(a>=b && b>=c)
		{
			System.out.println("Decreasing order");
		}
        else{
        	System.out.println("Neither increasing or decreasing");}

	}
}