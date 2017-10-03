class TreeNode:
	def __init__(self):
		self.parent=None
		self.left=None
		self.right=None
		self.key=None
class BinarySearchTree:
	def __init__(self):
		self.root=TreeNode()
	def search(self,k):
		temp=self.root
		while temp!=None:
			if k==temp.key:
				return temp
			if k>temp.key:
				temp=temp.right
			elif k<temp.key:
				temp=temp.left
		return None
	def minimum(self,x):
		temp=x
		while(temp!=None):
			y=x
			temp=temp.left
		return y.key
	def maximum(self,x):
		temp=x
		while(temp!=None):
			y=x
			temp=temp.right
		return y.key
	def sucessor(self,k):
		temp=self.search(k)
		if temp.right!=None:
			return self.maximum(temp.right)
		y=temp.parent
		while ((temp==y.right) and (y!=None)):
			temp=y
			y=temp.parent
		return y 
	def predecessor(self,k):
		temp=self.search(k)
		if temp.left!=None:
			return self.maximum(temp.left)
		y=temp.parent
		while ((temp==y.left) and (y!=None)):
			temp=y
			y=temp.parent
		return y 
	def insert(self,k):
		if self.root.key==None:
			self.root.key=k
			return
		x=self.root
		z=TreeNode()
		z.key=k
		#y=x.parent
		while x!=None:
			y=x
			if k<x.key:
				x=x.left
			else:
				x=x.right
		z.parent=y
		if k>y.key:
			y.right=z
		else:
			y.left=z
	def delete(self,k):
		node=self.search(k)
		if node.left==None and node.right==None:
			y=node.parent
			#print("leaf")
			if y.right==node:
				y.right=None
			else:
				y.left=None
		elif node.left==None and node.right!=None or node.left!=None and node.right==None:
			#print("1 child")
			y=node.parent
			if node.right!=None:
				node.right.parent=y
				if y.left==node:
					y.left==node.right
				elif y.right==node:
					y.right==node.right
			elif node.left!=None:
				node.left.parent=y
				if y.left==node:
					y.left==node.right
				elif y.right==node:
					y.right==node.right	
			node.parent=None
			node.left=None
			node.right=None
		elif node.left!=None and node.right!=None:
			#print("2 child")
			y_ref=self.predecessor(node.key)
			#y_ref=self.search(y)
			#print("@@@@@")
			#print(node)
			#print("@@@@@")
			#print("@@@@@")
			#print(y_ref)
			#print("@@@@@")
			self.delete(y_ref)
			node.key=y_ref
			#self.delete(y_ref)
	def traverse(self,x):
		if x==None:
			return
		else:
			print(x.key)
			self.traverse(x.left)
			self.traverse(x.right)
	def post(self,x):
		if x==None:
			return
		else:
			if x.key in ['+','-','*','/']:
				x=x.left
				self.post(x)
				x=x.parent
				x=x.right
				self.post(x)
				x=x.parent
				print(x.key)
			else:
				print(x.key)
	def eval(self,x):
		if x.left==None and x.right==None:
			return x.key
		else:
			op1=self.eval(x.left)
			op2=self.eval(x.right)
			result=self.apply(op1,op2,x.key)
			return result
	def apply(self,op1,op2,op):
		if op=='+':
			ans=int(op1)+int(op2)
		elif op=='-':
			ans=int(op2)-int(op1)
		elif op=='*':
			ans=int(op2)*int(op1)
		elif op=='/':
			ans=int(op2)/int(op1)
		return ans
def main():
	t=BinarySearchTree()
	expression=input()
	exp=list(expression)
	temp=t.root
	for i in exp:
		if i=="(":
			temp1=TreeNode()
			temp.left=temp1
			temp1.parent=temp
			temp=temp.left
		elif i in ['+','-','/','*']:
			temp.key=""
			temp.key+=i
			temp1=TreeNode()
			temp.right=temp1
			temp1.parent=temp
			temp=temp.right
		elif i==")":
			temp=temp.parent
		else:
			temp.key=""
			temp.key+=i
			temp=temp.parent
	t.traverse(t.root)
	#print(out)
	print("************")
	t.post(t.root)
	print("answer:",t.eval(t.root))
if __name__ == '__main__':
    	main()   
