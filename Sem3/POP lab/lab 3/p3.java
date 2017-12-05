import java.util.Scanner;
class p3
{
	public static void main(String args[])
	{
		Scanner input = new Scanner(System.in);
		System.out.println("Enter number of elements");
		int n=input.nextInt();
		int[] a= new int[n];
		int i;
		for(i=0;i<n;i++)
		{
			a[i]=input.nextInt();
		}
		int j,t;
		for(i=0; i < n; i++)
		{  
              for(j=1; j < (n-i); j++){  
                          if(a[j-1] > a[j]){  
                       
                                 t = a[j-1];  
                                 a[j-1] = a[j];  
                                 a[j] = t;  
                         }  
                          
                 }  
         }  
		//for(i=0;i<n;i++)
		//{
			//System.out.println(a[i]);
		//}
         int[] c=new int[n];
        for(i=0;i<n;i++)
        {  c[i]=0;
        	//System.out.println("hi");
        	for(j=i;j<n;j++)
        	{//System.out.println("hello");
        		if(j!=n-1)
        	   {if(a[j+1]-a[j]==1)
        		{
                      c[i]++;
                      //i=i+c[i];
        		}
        		
        		else {i=i+c[i]+1;//System.out.println("%%"+i);
        	       }
        	}
        	}
        }
        int max=-1,min=56000;
        for(i=0;i<n;i++)
              { //System.out.println("*"+c[i]); 
              	if(c[i]!=0)
              	{
              	if(c[i]>max)max=c[i];
              	else if(c[i]<min)min=c[i];
              }
             }
         System.out.println(max+1);
         if(min!=56001)System.out.println(min+1);
         else System.out.println("0");
	}
}