import java.util.Scanner;
import java.util.*;
class Page
{  int size;
	int id;
	boolean free;
    Page next;
	Page(int size,int id,boolean free)
	{
		this.size=size;
		this.id=id;
		this.free=free;
		this.next=null;
	}
}
class p1
{   
	public static void main(String args[])
	{   System.out.println("Frames?");
		Scanner input=new Scanner(System.in);
		int n=input.nextInt();
		int[] frames=new int[n];
	   System.out.println("process?");
        int p=input.nextInt();
	    int i=0;
        ArrayList<Page> process = new ArrayList<Page>(p);
	    for(i=0;i<n;i++)
	    {   
	    	process.add(new Page(54,i,true));
	    }
	}
}