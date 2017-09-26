import java.util.Scanner;
class p
{
	static int n=0;
	static int n1=0;
	static int n2=0;
	static int n3=0;
	static void fiction(String s)
	{   n1+=1;
        n+=1;
        System.out.println("Name of author:"+s);
	}
	static void non_fiction(String s)
	{   n2+=1;
		n+=1;
		System.out.println("Name of author:"+s);
	}
    static void scifi(String s)
    {   n3+=1;
    	n+=1;
    	System.out.println("Name of author:"+s);
    }

}
class p2
{
	public static void main(String[] args)
	{int i=0;
		for(i=0;i<5;i++)
		{System.out.println("Enter the author's name of the book you want to add:");
		Scanner input = new Scanner(System.in);
		String s=input.nextLine();
		System.out.println("Enter the genre (1.fiction,2.non fiction,3.scifi)");
		int c=input.nextInt();
		p obj=new p();
		switch(c)
		{
			case 1:  p.fiction(s);break;
			case 2:  p.non_fiction(s);break;
			case 3:  p.scifi(s);break;
			default: System.out.println("invalid option");break;
		}

        }
        System.out.println("Total nunmber of fiction books "+p.n1);
        System.out.println("Total nunmber of non fictional books "+p.n2);
        System.out.println("Total nunmber of scifi books "+p.n3);
        System.out.println("Total nunmber of books "+p.n);
	}
}