import java.util.Scanner;
class volume{
	double volume;
	public  void vol(int a)
	{
		this.volume=a*a*a;
		System.out.println(volume);
	}
	public void vol(int a,int h)
	{
		this.volume=3.14*a*a*h;
		System.out.println(volume);

	}
	
	public  void vol(int a,int b,int c)
	{
		this.volume=a*b*c;
		System.out.println(volume);

	}

	public static void main(String args[]){
		volume cube=new volume();
		volume cone=new volume();
		volume cylinder=new volume();
		volume cuboid=new volume();
		Scanner input=new Scanner(System.in);
		System.out.println("length of cube in int");
		int a=input.nextInt();
		int h;
		cube.vol(a);
		System.out.println("radius and height of cylinder in int");
		a=input.nextInt();
		h=input.nextInt();
		cylinder.vol(a,h);
		System.out.println("lemgth,breadth,height of cuboid");
		a=input.nextInt();
		int b=input.nextInt();
		int c=input.nextInt();
		cuboid.vol(a,b,c);
	}
}