class TrieNode:
    def __init__(self,v=None):
        self.value=v
        self.children=[]
        self.childNodes=[]
        self.eow=[]
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word,line,char):
        t=self.root
        for i in word:
            if i in t.children:
                t=t.childNodes[t.children.index(i)]
            else:
                t.children.append(i)
                t.childNodes.append(TrieNode(i))
                t=t.childNodes[-1]
        t.eow.append((line,char))
    
    def search(self,word):
        t=self.root
        for i in word:
            if i in t.children:
                t=t.childNodes[t.children.index(i)]
            else:
                return []
        return t.eow

def main():
    f=open('input.txt','r')
    l=0
    T=Trie()
    for line in f:
        l+=1
        char=1
        for i in line.split():
            T.insert(i,l,char)
            char+=len(i)
    ch=1
    while ch!=2:
        print("1.Search\n2.Quit")
        ch=int(input())
        if ch!=2 :
            w=input("Enter word:")
            slist=T.search(w)
            if slist==[]:
                print("Not Found!")
            else:
                for i in slist:
                    print("Found at line",i[0],"character",i[1])
            #print(slist)
                
    print("Thank You for using this program!")
    import time
    time.sleep(3)

if __name__=='__main__':
    main()