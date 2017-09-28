import java.util.Scanner;
class Org{
    String orgname = "xyz.org";
}
class Employee extends Org{
    String name;
    char grade;
    int age;
    int salary;
    Employee(String name,char grade,int age){
        this.name = name;
        this.grade = grade;
        this.age = age;
    }
    public void appraisal(){
        switch(grade){
            case 'a': salary = 60000;
                    break;
            case 'b': salary = 50000;
                    break;
            case 'c': salary = 40000;
                    break;
            default: salary = 30000;
        }
    }
    public void display(){
        System.out.println(name + " working for " + orgname + "has salary" + salary);
    }
}
class main{
    public static void main(String[] args){
        Employee Ea = new Employee("abc",'a',25);
        Employee Eb = new Employee("bbc",'b',35);
        Employee Ec = new Employee("cbc",'c',45);
        Employee Ed = new Employee("dbc",'d',55);
        System.out.println("After appraisal...");
        Ea.appraisal();
        Ea.display();
        Eb.appraisal();
        Ec.appraisal();
        Ed.appraisal();
        Eb.display();
        Ec.display();
        Ed.display();
    }
}