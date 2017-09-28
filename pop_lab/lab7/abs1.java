import java.util.Scanner;
class abs1
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        SBI s1 = new SBI();
        s1.deposit(1000);
        s1.withdraw(400);
        s1.calculation(1000);
        HDFC h1 = new HDFC();
        h1.deposit(1000);
        h1.withdraw(400);
        h1.calculation(1000);
    }
}
abstract class bank
{
    int d;
    void deposit(int d)
    {
        if (d>0)
        System.out.println("Deposited");
    }
    void withdraw(int w)
    {
        System.out.println("Withdrawed money: " +w);
    }
    abstract void calculation(int d);
}
class SBI extends bank
{
    double p;
    int d;
    void calculation(int d)
    {
        System.out.println("Deposited amount: "+d);
        p=d+(d*1.34);
        System.out.println("Amount after 2 yrs: "+p);
    }
}
class HDFC extends bank
{
    double p;
    int d;
    void calculation(int d)
    {
        System.out.println("Deposited amount: "+d);
        p=d+(d*1.04);
        System.out.println("Amount after 2 yrs: "+p);
    }
}