import java.util.Scanner;

public class prog2b
{
	public static void main ( String[] args)
	{
		Scanner s = new Scanner(System.in);
		int num,i = 0;
		int[] bin = new int[16];
		System.out.println("Enter a number : \n");
		num = s.nextInt();
		int temp = num;
		while(temp!=0)
		{
			if(temp % 2 == 0)
				bin[i] = 0;
			else
				bin[i] = 1;
			i++;
			temp/=2;
		}
		for(; i >= 0; i--)
			System.out.print(bin[i]);
		System.out.println("");
	}
}