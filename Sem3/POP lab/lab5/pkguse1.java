import java.util.Scanner;
import Student.NewClass;
class pkguse1{
    
    public static void main(String args[]){
     
        Scanner in=new Scanner(System.in);
        int choice=4;
        int[] info=new int[5];
        while(choice!=3){
        System.out.println("Choose the subject for marking attendance:\n1.Math\t2.Literature\n3.QUIT");  
        choice=in.nextInt();
        
        if(choice==1){
            
              System.out.print("Enter the number of students taking the course: ");
              int n=in.nextInt();
            for(int j=0;j<n;j++){
            in.nextLine();
            System.out.print("Enter their details:\nNAME: ");
            String name=in.nextLine();
            System.out.print("\nROLL NO: ");
            int rn=in.nextInt();
            
            NewClass s1=new NewClass(name,rn,"Math");     
            s1.SetN(n);
            for(int i=1;i<=5;i++)
            {
                 System.out.println("Class "+i+": Attended ?(Y/N)");
                 char yn=in.next().charAt(0);
                 if(yn=='y')
                     info[i-1]=1;
                 else
                     info[i-1]=0;
            }
            s1.SetPR(info);
            
            s1.Attendance();
            
        }
        }
        
        if(choice==2){
            
        System.out.print("Enter the number of students taking the course: ");
        int n=in.nextInt();
        for(int j=0;j<n;j++){    
            in.nextLine();
            System.out.print("Enter their details:\nNAME: ");
            String name=in.nextLine();
            System.out.print("\nROLL NO: ");
            int rn=in.nextInt();
            
            NewClass s2=new NewClass(name,rn,"Literature");     
            s2.SetN(n);
            for(int i=1;i<=5;i++)
            {
                 System.out.println("Class "+i+": Attended ?(Y/N)");
                 char yn=in.next().charAt(0);
                 if(yn=='y')
                     info[i-1]=1;
                 else
                     info[i-1]=0;
            }
            s2.SetPR(info);
            s2.Attendance();
        }
        }
     }
    }
}