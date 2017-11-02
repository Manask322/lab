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

def main():
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


if __name__ == '__main__':
    main()