abstract class Books{
    
    protected String Name;
    abstract public void Number(int a); 
    
}

abstract class Publishers extends Books{
    protected String company;
}

class Mystery extends Publishers{
    
    public Mystery(){
        super();
        this.Name="The ABC Murders";
        this.company="Bridge Works";
    }
    
    public Mystery(String company){
        super();
        this.Name="The ABC Murders";
        this.company=company;
    }
    
    public void Number(int n){
        System.out.println("The Mystery Genre book titled "+Name+" published by "+company+" is available now!\n"+n+" Copies.\n");
    }
    
}

 class Comedy extends Publishers{
    
    public Comedy(){
        super();
        this.Name="Three Men in a Boat";
        this.company="J. W. Arrowsmith";
    }
    
    public Comedy(String company){
        super();
        this.Name="Three Men in a Boat";
        this.company=company;
    }
    
    public void Number(int n){
        System.out.println("The Mystery Genre book titled "+Name+" published by "+company+" is available now!\n"+n+" Copies.\n");
    }
    
}

 class One {
        public static void main(String args[]){
         
            Mystery book1=new Mystery();
            Comedy book2=new Comedy();
            
            book1.Number(6);
            book2.Number(3);
            
            book1=new Mystery("Collins Crime Club");
            book2=new Comedy("None");
            
            book1.Number(7);
            book2.Number(8);
            
        }
}
