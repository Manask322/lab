class A
{
    int i;
    public A(int i)
    {
        this.i = i;
    }
    protected void finalize()
    {
        System.out.println("From Finalize Method, i = "+i);
    }
}
final class mul
{
  int b;
  mul(int l)
  {
    b=l;
  }

  final int mull(int n)
  {
    return n*b;
  }
} 
class Test
{
   public static void main(String[] args)
   {
       A a1 = new A(10);
       A a2 = new A(20);      
       //Assigning a2 to a1
       a1 = a2;
       System.gc();          
       System.out.println("Finalized!");
       mul obj = new mul(6);
       System.out.println("ans = " + obj.mull(5));
   }
}