import java.util.Scanner;
import java.util.*;
import node1.node;
public class main {
    static Scanner input=new Scanner(System.in);
    //The page table is created using a hash table.
    static Hashtable<String,ArrayList> table=new Hashtable<String,ArrayList>(15);
    static ArrayList<node> process=new ArrayList<node>(15);
    //A display header function.
    static void display(){
        for(int i=0;i<process.size();i++){
            if(process.get(i)!=null){
                System.out.println("|meamory:"+i+" processname:"+process.get(i).name+" pageno:"+process.get(i).pageno+"|");
            }else{
                System.out.println("|meamory:"+i+"|");
            }
        }
    }
    //A function to delete a process
    static void delete1(String p)
    {
        ArrayList<Integer> temp=table.get(p);//Get the entry containg the ArrayList of frame indices for all the pages int the process.
        for(int i=0;i<temp.size();i++)
        {
            process.set(temp.get(i),null);//Iterate the ArrayList and delete the page in the frame.
        }
        table.remove(p);//Remove the entry from the page table.
    }
    static void allocate(int processsize,String name)
    {
        int noofpages=processsize/50;
        node head=new node(-1);
        node tail = head;
	//Create an Array list that will store the frame indices of the pages in the process.
        ArrayList<Integer> temp=new ArrayList<Integer>(processsize);
        for(int j=0;j<noofpages;j++){
            for(int k=0;k<15;k++){
                if(process.get(k)==null){
                    process.set(k,new node(-1));//Set the value of the frame index at the location to be the address of the page it is storing.
                    process.get(k).pageno=j;
                    process.get(k).name=name;
                    temp.add(k);//Append the the frame indice in which the page is stored to the array.
                    break;
                }
            }
        }
        table.put(name,temp);//Add the whole array to the table.
    }
    public static void main(String args[]){
        int processsize[]=new int[]{100,50,210,120};
        for(int i=0;i<15;i++){process.add(i,null);}
        for(int i=0;i<processsize.length;i++){
            allocate(processsize[i],Integer.toString(i));
        }
        display();
        delete1("2");
        delete1("0");
        System.out.println("--------------------------------------------------");
        display();
        allocate(300,"google");
        System.out.println("--------------------------------------------------");
        display();
        System.out.println(table);
    }
}
