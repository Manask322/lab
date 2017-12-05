interface c1
{
	void message1();
    void message();
}
abstract class Abstractclass implements c1
{   
	public void message1(){
		
	}
    public void  message(){

    }
}
class c2 extends Abstractclass
{
	public void message()
	{
		System.out.println("This mesage was not implemented in the abstract class");
	}
		public void message1()
	{
		System.out.println("This mesage was not implemented in the abstracr class");
	}
}
class p5 
{
	public static void main(String[] args)
	{
        c2 obj = new c2();
        obj.message();
        obj.message1();
	}
}