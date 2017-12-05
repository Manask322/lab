import java.util.Scanner;
class p
{
static String pr1;
static String pr2;
static int q1;
static int q2;
static void getp()
{
System.out.println("Enter the two products");
Scanner input = new Scanner(System.in);
pr1=input.next();
pr2=input.next();
System.out.println("Enter the two product quantity");
q1=input.nextInt();
q2=input.nextInt();
}
static void printp()
{
	System.out.println("The two products are:");
	System.out.println(pr1);
	System.out.println(pr2);
	System.out.println("the quantities of the products are");
	System.out.println(q1);
	System.out.println(q2);
    
}

}
class p1
{
	public static void main(String args[])
	{
		p.getp();
		p.printp();
	}
}