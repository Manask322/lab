import java.lang.Math;

interface MyInterface {
  int a=10;
  public static int b=5;  
  public void add();
  public void sub();
  public void show();
}

interface Interface1{
    
    public void root();
}

interface Interface2 extends Interface1{
    
     public void power();
     
}
interface MarkerInt extends MyInterface,Interface2{
    //Empty;
}

class MyInterfaceAdapter implements MarkerInt{
    
    public void add(){}
    public void sub(){}
    public void show(){}
    public void power(){}
    public void root(){}

}
class UsingAdapter extends MyInterfaceAdapter{    
    
    public void add(){
        
        System.out.println("Adding 2 to the first number "+a+" is:"+(2+a));
        System.out.println("The sum of "+(2+a)+" and "+b+" is "+(a+b+2)+".");
    }
    
    public void root(){
        
        System.out.println("The square root of "+b+" is "+Math.sqrt(b)+".");
    }
    
    interface InnerIf{
        
        public void mul();
        public void div();
        
        interface Inner1{
            
            public void log();
            
        }
        
    }
}

abstract class UsingInnerIf implements UsingAdapter.InnerIf.Inner1{
    int n=56,x=450,y=132;
    
    abstract public void mul();
    
    abstract public void log();
}

class UseAbstract extends UsingInnerIf{
    
    public void mul(){
        
        System.out.println("The product of "+x+" and "+y+" is "+(x*y)+".");
    }   
    
    public void log(){
        
        System.out.println("The logarithmic value of "+n+" is "+Math.log(n)+".");
    }
    
}
class Main{
    
    public static void main(String args[]){
        
        MyInterfaceAdapter obj1=new UsingAdapter();
        obj1.add();
        obj1.root();
        
        UsingInnerIf obj2=new UseAbstract();
        obj2.log();
        obj2.mul();
        
    }
    
}