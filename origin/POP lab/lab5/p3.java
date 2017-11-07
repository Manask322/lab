import java.util.Scanner;
class p3
{
	public static void main(String args[])
	{
        int[] hex= new int[100];
        System.out.println("Enter the number");
        Scanner input = new Scanner(System.in);
        int n=input.nextInt();
        int i=0;
        while(n!=0)
        {
           hex[i]=n%16;
           n=n/16;
           i++;
        }
        i--;
        for(;i>=0;i--)
        {
        	if(hex[i]<=9)System.out.print(hex[i]);
        	else if(hex[i]==10)System.out.print("A");
        	else if(hex[i]==11)System.out.print("B");
        	else if(hex[i]==12)System.out.print("C");
        	else if(hex[i]==13)System.out.print("D");
        	else if(hex[i]==13)System.out.print("E");
        	else if(hex[i]==14)System.out.print("F");
        }
        System.out.println();
	}
}