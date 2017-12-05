class BinaryHeaps:
    def __init__(self,in_list=[]):
        self.arr=in_list
        self.top=-1
        self.build_heap(in_list)
    def pi(self, index):
        return (index - 1) // 2 if index != 0 else None
    def li(self, index):
        return 2 * index + 1 if 2 * index + 1 <= self.top else None
    def ri(self, index):
        return 2 * index + 2 if 2 * index + 2 <= self.top else None
    def swap(self,index1,index2):
        self.arr[index1],self.arr[index2]=self.arr[index2],self.arr[index1]
    def build_heap(self,in_list=[]):
        self.arr = in_list
        self.top=len(in_list)-1
        if self.top <= 0: 
            return
        for i in range(self.pi(self.top), -1, -1):
            self.heapify(i)
    def heapify(self,i):   
        li=self.li(i)
        ri=self.ri(i)
        if li is None and ri is None:
            return None
        elif li is None or ri is None:
            maxi = li if ri is None else ri
        else:
            maxi=li if self.arr[li]>self.arr[ri] else ri
        if self.arr[i]<self.arr[maxi]:
            self.swap(i,maxi)
            self.heapify(maxi)
    def extract_max(self):
        x=self.arr[0]
        self.swap(0,self.top)
        self.top-=1
        self.heapify(0)
        return x
# def bsort(self,a=[]):
#     bh=BinaryHeaps(a)
#     for i in range(len(a)-1,0,-1):
#         a[i]=bh.extract_max()
#         print(a[i])
#     return a
# def main():
#     a=[-5,7,-3,60,89]
#     a=bsort(a)
#     print(a)
def main():
    a=[34,-9,45,5]
    bh=BinaryHeaps(a)
    # for i in range(4):
    #     print(bh.extract_max())
    for i in range(len(a)-1,0,-1):
        a[i]=bh.extract_max()
    print(a)
main()