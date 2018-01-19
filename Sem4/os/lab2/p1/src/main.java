import java.util.Scanner;
import java.util.*;
import node1.node;
public class main {
    static Scanner input=new Scanner(System.in);
    static ArrayList<node> process=new ArrayList<node>(15);
    static void display(){
        for(int i=0;i<process.size();i++){
            if(process.get(i)!=null){
                System.out.println("|meamory:"+i+" processname:"+process.get(i).name+" pageno:"+process.get(i).pageno+"|");
            }else{
                System.out.println("|meamory:"+i+"|");
            }
        }
    }
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
        if(temp==-1)
        {
            System.out.println("No process found");
            return;
        }
        node pointer = process.get(temp);
        while(pointer!=null)
        {
            int index=pointer.addr;
            process.set(index,null);
            pointer=pointer.next;
        }
    }
    static void allocate(int processsize,String name)
    {

        //process.add(i,new node());
        int noofpages=processsize/50;
        node head=new node(-1);
        node tail = head;

        for(int j=0;j<noofpages;j++){
            for(int k=0;k<10;k++){
                if(process.get(k)==null){
                    process.set(k,new node(-1));
                    process.get(k).pageno=j;
                    process.get(k).name=name;
                    process.get(k).addr=k;
                    tail.next=process.get(k);
                    tail=process.get(k);break;
                }
            }
        }

    }


    public static void main(String args[]){
        int processsize[]=new int[]{100,50,210,120};
        for(int i=0;i<10;i++){process.add(i,null);}
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

    }

}
