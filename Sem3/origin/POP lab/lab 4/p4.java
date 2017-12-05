import java.util.Scanner;
class semester
{   String name;
	int marks1;
	int marks2;
	semester(String s,int m1,int m2)
	{
        this.name=s;
        this.marks1=m1;
        this.marks2=m2;
	}
	public void getsem1()
	{
         System.out.println("the marks of "+this.name+" in first semester :"+this.marks1);
	}
	public void getsem2()
	{ 
		System.out.println("the marks of "+this.name+" in second semester :"+this.marks2);
	}
}
class p4
{

public static void main(String args[])
{
   semester s1 = new semester("abc",98,99);
   semester s2= new semester("xyz",100,97);
   s1.getsem1();
   s1.getsem2();
   s2.getsem1();
   s2.getsem2();
}

}