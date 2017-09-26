import java.util.Scanner;
class common{
	public static void main(String[] args){
		int a[]=new int[20];
		int b[]=new int[20];
		int c,d,temp,i;
		Scanner input=new Scanner(System.in);
		System.out.println("enter the size of array1");
		c=input.nextInt();
		System.out.println("enter the size of array2");
		d=input.nextInt();
		System.out.println("enter the elements of array1");
		for(i=0;i<c;i++){
			a[i]=input.nextInt();
		}
		System.out.println("enter the elements of array1");
		for(i=0;i<d;i++){
			b[i]=input.nextInt();
		}
		for(i=0;i<c;i++)
		{
			temp=a[i];
			for(int j=0;j<d;j++){
				if(temp==b[j])
					System.out.println(temp+"is common");
			}
		}
		
	}
}