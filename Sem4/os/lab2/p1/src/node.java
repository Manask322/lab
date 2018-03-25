package node1;
public class node{
    //Attributes of a page.
    public int processno;
    public int pageno;
    public node next;
    public String name;
    public int addr;
    //A constructor
    public node(int processno){
        this.processno=processno;
        //this.pageno=pageno;
        this.next=null;
    }

}
