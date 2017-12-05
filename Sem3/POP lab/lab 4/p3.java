import java.util.Scanner;
class p3
{
	public static void main(String args[])
	{
       Scanner input = new Scanner(System.in);
       System.out.println("Enter size ");
       int n=input.nextInt();
       System.out.println("Enter array");
       int[] a = new int[n];
       int i;
       for(i=0;i<n;i++)a[i]=input.nextInt();
       System.out.println("Enter serch element");
       int k=input.nextInt();
       int ans=0,flag=0;
       for(i=0;i<n;i++)
       {
       	if(a[i]==k){ans=i;flag=1;break;}
       }	
       if(flag!=0)System.out.println(ans);
       else System.out.println("element not found");
	}
}