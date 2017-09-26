import java.util.Scanner;
class p5
{
void dep1(int bp)
{
System.out.println("your increment in managing "+(bp+10000));
}
void dep2(int bp)
{
System.out.println("your increment in directing "+(bp+100000));
}
void dep3(int bp)
{
System.out.println("your increment in public allowances "+(bp+1000000));
}
public static void main(String args[])
{
System.out.println("enter basic pay");
Scanner sc=new Scanner(System.in);
int bp=sc.nextInt();
p5 ob1=new p5();
p5 ob2=new p5();
p5 ob3=new p5();
ob1.dep1(bp);
ob2.dep2(bp);
ob3.dep3(bp);
}
}