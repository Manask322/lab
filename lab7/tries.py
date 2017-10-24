class TrieNode:
    def __init__(self,v=None):
        self.value=v
        self.children=[]
        self.childNodes=[]
        self.eow=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        t=self.root
        for i in word:
            if i in t.children:
                t=t.childNodes[t.children.index(i)]
            else:
                t.children.append(i)
                t.childNodes.append(TrieNode(i))
                t=t.childNodes[-1]
        t.eow=True
    
    def search(self,word):
        t=self.root
        for i in word:
            if i in t.children:
                t=t.childNodes[t.children.index(i)]
            else:
                return False
        return t.eow

def main():
    T=Trie()
    r=input("Enter sentence:")
    for i in r.split(' '):
        T.insert(i)
    s=input("Enter search word:")
    print(T.search(s))

if __name__=='__main__':
    main()
        