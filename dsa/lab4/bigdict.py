class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode();

    def insert(self,x,p,v):
        """Insert element x in the position after p"""
        
        temp=ListNode()
        temp.value=x
        temp.next=p.next
        p.next=temp


    def delete(self,p):
        """Delete the node following node p in the linked list."""
        print("deleting node at given position")
        temp=p.next
        p.next=temp.next

    def printlist(self):
        """ Print all the elements of a list in a row."""
        print("List is",end=' ')
        temp=self.head.next
        while temp!=None:
            print(temp.value,end=' ')
            temp=temp.next
        print()



    def insertAtIndex(self,x,i,v):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        ''' i will stop at one position priror'''
        t=0
        temp=self.head
        while(t<i):
            temp=temp.next
            t=t+1
        '''normal insert pos'''
        p=temp
        temp=ListNode()
        temp.value=x
        temp.next=p.next
        p.next=temp
        temp.key=v

    def search(self,x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp=self.head.next
        while temp!=None:
            if temp.value==x:
                print("element found",end=' ')
                return temp
            temp=temp.next
        return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        len=0
        temp=self.head.next
        while temp!=None:
            len=len+1
            temp=temp.next
        return len

        

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
    def __init__(self,val=None,nxt=None,ky=None):
        self.value=val
        self.next=nxt
        self.key=ky
####linked list above
class hashtable:

	def __init__(self):
		self.T=[None for i in range(0,1000)];
	def hashvalue(self,string):
		h=0
		for i in range(len(string)-1,-1,-1):
			h=h*33+ord(string[i])
		h=h%999
		return(h)
	def inserthash(self,string):
		v=self.hashvalue(string)
		if(self.T[v]==None):
			self.T[v]=LinkedList()
			self.T[v].insert(string,self.T[v].head,v)
		else:
			self.T[v].insert(string,self.T[v].head,v)
	def display(self):
		print("#############3##hash table display starts ###################################################")
		for i in range(0,len(self.T)):
			if self.T[i]!=None:
				print(i,"   ",end=' ')
				self.T[i].printlist()
			else:
				print(i,"None")
		print("#############3##hash table display ends ###################################################")
	def searchhash(self,string):
		v=self.hashvalue(string)
		if self.T[v]==None:
			print("not valid")
		else:
			addr=self.T[v].search(string)
			if addr==None:
				print("not valid")
			else:
				print("at",addr,"hash table index is",v,"valid")
	def keyhash(self):
		for i in range(0,len(self.T)):
			if self.T[i]==None:
				print("None",end=" ")
			else:
				print(i,end=' ')
		print()



def main():
    a=hashtable()
    with open("ispell.dict","r") as f:
        for line in f:
            string=line.split();
            a.inserthash(string[0])
    #a.display()
    c=True
    print("enter elements to be searched or enter space to exit")
    while c:
        s=input()
        if s==' ':
            c=False
        else:
            a.searchhash(s)


if __name__ == '__main__':
	main()
