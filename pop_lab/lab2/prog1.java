import java.util.Scanner;

public class prog1
{
	public static void main( String[] args)
	{
		Scanner s = new Scanner(System.in);
		int choice, a, b;
		System.out.println("Enter your operation : \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n");
		choice = s.nextInt();
		System.out.println("Enter numbers : ");
		a = s.nextInt();
		b = s.nextInt();
		switch (choice)
		{
			case 1 : 
				System.out.println(a + "+" + b + "=" + (a+b));
				break;
			case 2 :
				System.out.println(a + "-" + b + "=" + (a-b));
				break;
			case 3 :
				System.out.println(a + "*" + b + "=" + (a*b));
				break;
			case 4 :
				System.out.println(a + "/" + b + "=" + ((float)a/b));
				break;
		}
	}
}