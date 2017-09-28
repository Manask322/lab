import java.util.Scanner;
class inter
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        c1 p = new c1();
        p.add(10,2);
        p.mul(10,2);
        B b1 = new B();
        b1.m2();
        A a1 = new A();
        a1.m1();
        C a2 = new C();
        a2.m1();
        a2.m2();
        D d2 = new D();
        d2.k1();
        d2.k2();
        d2.k3();
    }
}

interface i1
{
    public void add(int a,int b);
    public void mul(int a,int b);
}

class c1 implements i1
{
    int c;
    public void add(int a,int b)
    {
        c=a+b;
        System.out.println("Sum="+c);
    }
    public void mul(int a,int b)
    {
        c=a*b;
        System.out.println("Product="+c);
    }
}
class A
{
    void m1()
    {
        System.out.println("Class A method 1");
    }
    interface I1
    {
        public void m2();
    }
}
class B implements A.I1
{
    public void m2()
    {
        System.out.println("Class B interface method 2");
    }
}
class C extends A
{
    public void m2()
    {
        System.out.println("Class C interface method 2");
    }
}
interface i10
{
    public void k1();
    public void k2();
}
interface i11 extends i10
{
    public void k3();
}
class D implements i10,i11
{
    public void k1()
    {
        System.out.println("Class D interface method k1");
    }
    public void k2()
    {
        System.out.println("Class D interface method k2");
    }
    public void k3()
    {
        System.out.println("Class D interface method k3");
    }
}