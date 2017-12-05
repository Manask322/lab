import java.util.Scanner;
class prog3
{
	public static void main(String args[])
	{
        System.out.println("\nEnter the coefficients of the equations of the two equations of the form aX+bY=C\nEnter first equation coefficients");
        Scanner input=new Scanner(System.in);
        int a1,b1,c1,a2,b2,c2;
        a1=input.nextInt();
        b1=input.nextInt();
        c1=input.nextInt();
        System.out.println("Enter coefficients of the second equarion");
        a2=input.nextInt();
        b2=input.nextInt();
        c2=input.nextInt();
        if((float)a1/a2==(float)b1/b2 && (float)b1/b2==(float)c1/c2)
	    {
	    	System.out.println("Redundant euation");
	    }
	    else
        {
           float x=(c1*b2-b1*c2)/(a1*b2-a2*b1);
           float y=(a1*c2-a2*c1)/(a1*b2-a2*b1);
          System.out.println("X:"+x+"\nY:"+y);
	    }
	}
}