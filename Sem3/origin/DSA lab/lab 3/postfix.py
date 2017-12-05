class stack:
    def __init__(self):
        self.elements =[None]*45
        self.top=-1
    def push(self,x):
        if self.top==44:
            print("stack overflow")
            return
        else:
            self.top+=1
            self.elements[self.top]=x
    def pop(self):
        if self.top==-1:
            print("underflow")
            return
        else:
            self.top-=1
            return self.elements[self.top+1]
def isoperand(exp):
	if exp=='/' or exp=='*' or exp=='-' or exp=='+':
		return False
	else:
		return True
def apply(i,op1,op2):
    op1=int(op1)
    op2=int(op2)
    if i=='+':
        return op1+op2
    elif i=='-':
        return op2-op1
    elif i=='*':
        return op1*op2
    elif i=='/':
        return op2/op1


def main():
    s=stack()
    s1=input()
    exp=s1.split()
    for i in exp:
        if isoperand(i):
            s.push(i)
        else:
            op1=s.pop()
            op2=s.pop()
            result=apply(i,op1,op2)
            s.push(result)
    return s.pop()
            

if __name__ == '__main__':
    ans=main()
    print(ans)




