import java.util.Scanner;
abstract class pr
{
	abstract void calculation(int p,int t);
	abstract void interest();
	abstract void display();
}
class sbi extends pr
{   float si;
	int r;
	sbi(int r)
	{
    this.r=r;
	}
	void calculation(int p,int t)
	{
		this.si=p*this.r*t/100;
	}
    void interest()
    {
        System.out.println("The interest of sbi is:"+this.r+"%");
    }
    void display()
    {
    	System.out.println("The simple interest amount in sbi is:"+this.si);
    }
}
class canara extends pr
{   float si;
	int r;
	canara(int r)
	{
    this.r=r;
	}
	void calculation(int p,int t)
	{
		this.si=p*this.r*t/100;
	}
    void interest()
    {
        System.out.println("The interest of canara bank is:"+this.r+"%");
    }
    void display()
    {
    	System.out.println("The simple interest amount in canara bank is:"+this.si);
    }
}
class hdfc extends pr
{   float si;
	int r;
	hdfc(int r)
	{
    this.r=r;
	}
	void calculation(int p,int t)
	{
		this.si=p*this.r*t/100;
	}
    void interest()
    {
        System.out.println("The interest of hdfc bank is:"+this.r+"%");
    }
    void display()
    {
    	System.out.println("The simple interest amount in hdfc bank is:"+this.si);
    }
}
class p2
{
	public static void main(String[] args)
	{   Scanner input =new Scanner(System.in);
		System.out.println("Enter the principal amount:");
		int p=input.nextInt();
		System.out.println("Enter the time in years:");
		int t=input.nextInt();
		sbi sobj=new sbi(5);
		sobj.calculation(p,t);
		sobj.interest();
		sobj.display();
		canara cobj=new canara(4);
		cobj.calculation(p,t);
		cobj.interest();
		cobj.display();
		hdfc hobj=new hdfc(6);
		hobj.calculation(p,t);
		hobj.interest();
		hobj.display();
	}
}