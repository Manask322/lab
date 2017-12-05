class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        sent=ListNode()
        self.head=sent
        

    def insert(self,x,p):
        """Insert element x in the position after p"""
        temp=ListNode()
        temp.value=x
        temp.next=p.next
        p.next=temp

    def delete(self,p):
        """Delete the node following node p in the linked list."""
        p.next=p.next.next

    def printl(self):
        """ Print all the elements of a list in a row."""
        
        temp=self.head.next
        while(temp!=None):
            print(temp.value)
            temp=temp.next

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp=self.head
        t=0
        while(t<i):
            temp=temp.next
            t+=1
        temp1=ListNode()
        temp1.value=x
        temp1.next=temp.next
        temp.next=temp1 
    def search(self,x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp=self.head.next
        while(temp!=None):
            if temp.value==x:
                return temp
            temp=temp.next
        return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        temp=self.head
        i=0
        while(temp!=None):
            i+=1
            temp=temp.next
        return i-1
    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.head.next==None:
            return True
        else:
            return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self):
        self.value=None
        self.next=None
#will not be used
def main1():
    L = LinkedList()
    L.insert(10,L.head)
    print("The list is:")
    L.printl()
    L.insert(12,L.head.next)
    print("The list is:")
    L.printl()
    L.insert(2,L.head)
    print("The list is:")
    L.printl()
    print("Enter search element")
    k=int(input())
    p=L.search(k)
    if(p==None):
        print("Element not found")
    else:            
        print("Element found")
    print('Size of L is ',L.len())
    L.delete(L.head)
    print("The list is:")
    L.printl()
    L.delete(L.head.next)
    print("The list is:")
    L.printl()
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print("The list is:")
    L.printl()

def main(): 
    t=[None for i in range(30)]
    
    def hash1(s):
        sum=0
        for i in s:
            sum+=ord(i)
        return sum%30
    def hash(s):
        p=0
        x=33
        for i in s[-1::-1]:
            p = p*x+ord(i)
        return p%30
    def hinsert(s):
        if(t[hash(s)]==None):
            L=ListNode()
            t[hash(s)]=L
            L.value=""
            for i in s:
                L.value+=i
            L.next=None
        else:
            L=ListNode()
            L.next=t[hash(s)]
            t[hash(s)]=L
            L.value=""
            for i in s:
                L.value+=i
    def keys(t):
        key=[None]*30
        for i in range(30):
            if t[i]!=None:
                key.append(i)
        return key
    """s=input()
    s0=input()
    s1=input()
    hinsert(s)
    hinsert(s0)
    hinsert(s1)
    print(t[hash(s)].value)
    print(t[hash(s)].next.value)
    print(t[hash(s)].next.next.value)
    print(t[hash(s)].next.next.next)
    """
    #a=keys(t)
    #for i in a:
        #if i!=None:
            #print(i)
    def search(s):
        if(t[hash(s)]==None ):
            print("  ***element not there")
        elif t[hash(s)]!=None:
            k=None
            temp=t[hash(s)]
            #print(type(temp))
            flag=0
            while(temp!=None):
                if(temp.value==s):
                    flag=1
                    break
                temp=temp.next 
            if(flag==1):
                print("element found at",t[hash(s)])
                return True
            else:
                print("element not there")
    #s1=input()
    #earch(s1)
    with open("small.dict","r") as ins:
        for line in ins:
            ss=line.split()
            hinsert(ss[0])
        # print column 
    #with open('small.dict','r') as inf:
        #for line in inf:
            #parts = line.split(" ") # split line into parts
            #if len(parts) > 1:   # if at least 2 parts/columns
                #hinsert(parts[1])   # print column 2
    s3=input()
    if(search(s3)):
        print("valid word")
    """
    s4=input()
    print(hash(s3))
    temp=t[hash(s3)]
    temp1=t[hash(s4)]
    while(temp!=None):
        print(temp.value)
        temp=temp.next
    print("*****")
    while(temp1!=None):
        print(temp1.value)
        temp1=temp1.next
      """  """
    for i in range(30):
        temp=t[i]
        while(temp!=None):
            print(temp.value)
            temp=temp.next
        print("***")
        """
    #a=keys(t)
    #for i in a:
        #if i!=None:
            #print(i)
    #print("*****",hash(s3))
if __name__ == '__main__':
    main()


