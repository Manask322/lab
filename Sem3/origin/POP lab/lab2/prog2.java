import java.util.Scanner;
class prog2
{
	public static void main(String args[])
	{
        Scanner input = new Scanner(System.in);
        System.out.println("\nEnter number");
        int num=input.nextInt();
        int n=num;
        int d=0;
        if(n%2!=0 || n%10==0)
        {  while(n!=0)
             {
                d=d*10+n%2;
                n=n/2;
              }
        }
        else
        {int c=-1;
        	while(num!=0)
        	{
                 num=num/2;
                 c+=1;
        	}
        d=1;
        int count=1;
        while(count<=c-1)
        {
        	d=d*10;
        	count++;
        }	

        }
        System.out.println(d);
	}
}