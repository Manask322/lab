import java.util.Scanner;
class p
{
   String sname;
   int[] marks=new int[5];
   int i;
   Scanner input = new Scanner(System.in);
   void get(p[] s)
   {
   	int i;
   	/*for(i=0;i<5;i++)
   	{
   		p s[i]=new p();
   	}*/
    int j;
    for(i=0;i<5;i++)
    {
    	System.out.println("Enter the name of the students");
    	s[i].sname=input.next();
    	System.out.println("Enter the marks of the students");
    	for(j=0;j<5;j++)
    	{
           s[i].marks[j]=input.nextInt(); 
    	}
    }
   }
   void add(p[] s)
   {
   	  int i=0,j;
   	  for(i=0;i<5;i++)
      {
      	System.out.println("marks of "+s[i].sname);
      	int sum=0;
      	for(j=0;j<5;j++)
      	{
      		sum+=s[i].marks[j];
      	}
      	System.out.println(sum);
      }
   } 
}
class p4
{
	public static void main(String args[])
	{
	int i=0;
	p[] s= new p[5];
    for(i=0;i<5;i++)
   	{
   		s[i]=new p();
   	}
    p student = new p();
    student.get(s);
    student.add(s);
	}
}