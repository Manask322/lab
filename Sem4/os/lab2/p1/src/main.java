import java.util.Scanner;
import java.util.*;
import node1.node;
public class main {
 
    static Scanner input=new Scanner(System.in);
    //Main memory containing the memory locations of pages.
    static ArrayList<node> process=new ArrayList<node>(15);
    //A helper display function
    static void display(){
  
        for(int i=0;i<process.size();i++){
            if(process.get(i)!=null){
                System.out.println("|meamory:"+i+" processname:"+process.get(i).name+" pageno:"+process.get(i).pageno+"|");
            }else{
                System.out.println("|meamory:"+i+"|");
            }
        }
    }
    //Function to allocate memory location for pages for that particular process
    static void delete1(String p)
    {   int temp=-1;
        for(int i=0;i<process.size();i++)
        {
            if(process.get(i)!=null && process.get(i).name.equals(p))
            {
                temp=i;
                break;
            }
        }
        //At the end of this for-loop we get the first page of the process.
        if(temp==-1)
        {
            System.out.println("No process found");
            return;
        }
        node pointer = process.get(temp);
        //We traverse all the subsequent pages of the process and delete the page from main memory
        while(pointer!=null)
        {
            int index=pointer.addr;
            process.set(index,null);
            pointer=pointer.next;
        }
    }
    //This function allocates a proess across frames
    static void allocate(int processsize,String name)
    {

        //Get the number of pages
        int noofpages=processsize/50;
        node head=new node(-1);
        node tail = head;
        //Allocate frames to each of those pages
        for(int j=0;j<noofpages;j++){
            for(int k=0;k<10;k++){
                //if memory space is free. 
                if(process.get(k)==null){
                    process.set(k,new node(-1)); //Set the memory location of the page to the main memory
                    process.get(k).pageno=j;     //Set all the attributes of the page.
                     process.get(k).name=name;   
                    process.get(k).addr=k;
                    tail.next=process.get(k);
                    tail=process.get(k);break;
                }
            }
        }

    }
    public static void main(String args[]){
    // An array of process.
        int processsize[]=new int[]{100,50,210,120};    
        for(int i=0;i<10;i++){process.add(i,null);}
        for(int i=0;i<processsize.length;i++){
        //allocate each proces.
            allocate(processsize[i],Integer.toString(i));
        }
        //Testing Functions
        display();
        delete1("2");
        delete1("0");
        System.out.println("--------------------------------------------------");
        display();
        allocate(300,"google");
        System.out.println("--------------------------------------------------");
        display();

    }

}
