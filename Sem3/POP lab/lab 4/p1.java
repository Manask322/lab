import java.util.Scanner;
class p1
{
	public static void main(String args[])
	{
       int n;
       String s=null;
       Scanner input= new Scanner(System.in);
       System.out.println("Enter the number");
       n=input.nextInt();
       if(n>0)
      {
       n=n%7;
       if(n==1)s="monday";
       else if(n==2)s="tuesday";
       else if(n==3)s="wednesday";
       else if(n==4)s="thursday";
       else if(n==5)s="friday";
       else if(n==6)s="saturday";
       else if(n==0)s="sunday";
       System.out.println("The day is: "+s);
   }else System.out.println("Invalid input");
	}
}