import java.util.Scanner;
class p2
{
	public static void main(String args[])
	{
		Scanner input = new Scanner(System.in);
		System.out.println("Enter principal, rate of interest,time");
		float p=input.nextFloat();
		float r=input.nextFloat();
		float t=input.nextFloat();
		int i;
		double ans;
		r=r/100;
		for(i=1;i<=t;i++)
		{
			ans=p*(Math.pow((1+r/12),12*i));
            System.out.println("Year: "+i+"   Amount:"+ans);
		}
	}
}