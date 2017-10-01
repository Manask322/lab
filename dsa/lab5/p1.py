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
def main():
	t=BinarySearchTree()
	t.insert(3)

	#print(t.root.key)
	t.traverse(t.root)
	print("************")
	t.insert(4)
	#print(t.root.right.key)
	t.traverse(t.root)
	print("************")
	t.insert(7)
	t.traverse(t.root)
	print("************")
	t.insert(2)
	t.traverse(t.root)
	print("************")
	print(t.search(2))
	#t.delete(2)
	t.traverse(t.root)
	print("***********")
	#print(t.predecessor(7).key)
	#print(t.maximum(t.root))
	#print(t.minimum(t.root))
	#print(t.sucessor(3))
	#print("@@@@@")
	#print(t.predecessor(3))
	#print("@@@@@")
	t.delete(7)
	t.delete(3)
	#print(t.search(7))
	print("***********")
	t.traverse(t.root)
	print("***********")
	#print(t.search(7))
	#print(t.search(7).left)
	#print(t.predecessor(4))
	t.delete(4)
	t.traverse(t.root)
if __name__ == '__main__':
    	main()    
