package Student;
public class NewClass{
    
    String Name;
    int Rollnum;
    String Class;
    int TOT[]=new int[5];
    int numst;
    
    public NewClass(String name,int num,String cl){
        Name=name;
        Rollnum=num;
        Class=cl;
    }
    
    public void SetN(int n){
     
        numst=n;
        
    }     
    
    public void SetPR(int pr[]){
        TOT=pr;
    }
    
    public void Attendance(){ 
            int sum=0;
            for(int i=0;i<5;i++)
               sum=sum+TOT[i];
            float perc=sum*100/5;
            System.out.println("Number of classes attended by "+Name+" (RollNumber:"+Rollnum+") out of 5 for "+Class+" is "+sum+": "+perc+"%.");
            if (perc < 75.0)
                System.out.println("\nAttendance less than 75%.\n");
            else
                System.out.println("\n");
         }
}


    



