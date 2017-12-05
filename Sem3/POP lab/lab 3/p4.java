import java.util.Scanner;
class p4
{
	public static void main(String args[])
	{
		Scanner input=new Scanner(System.in);
		System.out.println("enter size of two arrays");
		int n1= input.nextInt();
		int n2= input.nextInt();
		int[] a=new int[n1];
		int[] b=new int[n2];
		int[] c=new int[n2+n1];
		int i,j;
		for(i=0;i<n1;i++)
		{
            a[i]=input.nextInt();
		}System.out.println("Enter second array");
		for(i=0;i<n2;i++)
		{
            b[i]=input.nextInt();
            for(j=0;j<n1;j++)
            {
            	if(a[j]==b[i])
            		{
            			c[i]=b[i];
            			break;
            		}
            }
		}
	}
}