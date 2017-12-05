import java.util.Scanner;
class prog4
{
	public static void main(String args[])
	{
        int o,num,n;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number");
        num=input.nextInt();
        System.out.println("Enter by how many shifts");
        n=input.nextInt();
        System.out.println("\nYour choices\n1.Right shift unsigned\n2.Right shift\n3.Left shift");
        o=input.nextInt();
        int ans=0;
        switch(o)
        {
        	case 1: ans=num>>>n;
        	        break;
        	case 2: ans=num>>n;
        	        break;
        	case 3: ans=num<<n;
        	        break;
        	default: System.out.println("Wrong choice");

        }
        if(o==3||o==1||o==2)System.out.println("Answer:"+ans);
	}
}