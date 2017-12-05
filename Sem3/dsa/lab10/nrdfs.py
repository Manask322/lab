class node:    
    def __init__(self,key):
        self.val = key
        self.colour = 'white'
        self.next = None
        self.par = None
        self.start = None
        self.finish = None
class Graph:
    def __init__(self,v,e):
        # self.V = [None for i in range(v)]
        # self.E = {}
        # self.adjL = []     
        self.time = 1   
    def insertL(self,v,t):
        L = [None for i in range(v)]
        # print(len(t))
        # for i in range(v):
        #     L[i] = LinkedList()
        # for i in range(len(t)):
        #     u,w = t[i]
        #     L[u].insert(w)
        #     L[w].insert(u)  
  
        # for i in range(len(L)):
        #     print(i,end = ': ')
        #     L[i].printList()
        # return L
    def adjlist(self,n,e):
        a=[[] for x in range(n)]
        w=[[[56000] for x in range(n)]for x in range(n)]
        vertex=[None for x in range(n)]
        for i in range(n):
            vertex[i]=node(i)
        print("Enter edges")
        for i in range(e):
            u,v=tuple(input().split(' '))
            u,v= int(u),int(v)
            a[u].append(v)
            a[v].append(u)
        # for i in range(n):
        #   print("Vertex ",i,": ",a[i])
        return a,vertex
    def DFS(self,alist,V,s):
        V[s].start = self.time
        self.time+=1
        V[s].colour = 'grey'
        S = []
        S.append(s)
        while len(S) != 0:
            u = S.pop()      
            if V[u].colour is 'black':
                V[u].finish = self.time
                self.time+=1
                continue
            S.append(u)
            ptr = alist[u].head
            flag = False
            while ptr is not None:
                v = ptr.val
                if  V[v].colour is 'white':
                    flag = True
                    V[v].start = self.time
                    time+=1
                    V[v].colour = 'grey'
                    V[v].par = V[u]
                    S.append(v)
                    break
                ptr = ptr.next
            if flag == False:
                V[u].colour = 'black'
        return V   
def main():
    G=Graph(5,6)
    alist,vertex=G.adjlist(5,6)
    V=G.DFS(alist,vertex,0)
    for i in range(len(G.V)):
        print("Vertex " + str(i) + " : t1 " + str(V[i].start) + "  t2 : " + str(V[i].finish))
if __name__=='__main__':
    main()            
# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def printList(self):
#         """ Print all the elements of a list in a row."""
#         ptr = self.head
      
#         while ptr is not None:
#             print(ptr.val,end=' , ')
#             ptr = ptr.next
#         print("")     

#     def insert(self,x):
#         temp = vertex(x)
#         ptr = self.head
#         if ptr is None:
#             self.head = temp
#             return
#         while ptr.next is not None:
#             ptr = ptr.next
#         ptr.next = temp 
# def main():
#     num_v = int(input("Enter the number of vertices:"))
#     num_e = int(input("Enter the number of edges: "))
#     G = Graph(num_v, num_e)
#     for i in range(num_v):
#         G.V[i] = (vertex(i))    
#     print("Enter the edges:")
#     t = list()    
#     for i in range(num_e):
#         u,v = map(int, input().split())
#         t.append((u,v))
#     G.E = t
#     G.adjL = G.insertL(num_v,G.E)
#     sr = int(input('Enter the source vertex : '))
#     G.DFS(sr)
#     for i in range(len(G.V)):
#         print("Vertex " + str(i) + " : t1 " + str(G.V[i].start) + "  t2 : " + str(G.V[i].finish))

