import java.util.Scanner;
class check
{
	public boolean ten(int a[])
	{
		int i,sum=0;
		for(i=0;i<a.length;i++)
		{
           if(a[i]==10)
           {
           	sum+=10;
           }
		}
		if(sum==30)return true;
		else return false;
	}
}
class p2
{
  public static void main(String args[])
  {
  	Scanner input = new Scanner(System.in);
  	System.out.println("Enter size of the array");
  	int n= input.nextInt();
  	int[] a = new int[n];
  	System.out.println("Enter array");
    int i;
    for(i=0;i<n;i++)
    	{a[i]=input.nextInt();}
    check obj = new check();
     boolean ans=obj.ten(a);
     System.out.println(ans);
  }
}