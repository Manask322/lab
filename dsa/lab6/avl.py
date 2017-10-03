class TreeNode:
	def __init__(self):
		self.parent=None
		self.left=None
		self.right=None
		self.key=None
		self.height=None
class avl:
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
		node=z
		x=node
		y=x.parent
		z=y.parent
		while(z!=None and abs(self.h(z.right)-self.h(z.left))<=1):
			z=z.parent
			y=y.parent
			x=x.parent
		if y=z.left and x=y.left:
			z.left=y.right
			y.right.parent=z
			y.parent=z.parent
			z.parent=y
			y.right=z
			if y.parent==None:
				self.root=y
			else:
				if y.key > y.parent.key:
					y.parent.right=y
				else:
					y.parent.left=y
		elif y=z.right and x=y.right:
			z.right=y.left
			y.left.parent=z
			y.parent=z.parent
			z.parent=y
			y.left=z
			if y.parent==None:
				self.root=y
			else:
				if y.key > y.parent.key:
					y.parent.right=y
				else:
					y.parent.left=y
		elif y=z.left and x=y.right:
			y.right=x.left
			x.left.parent=y
			y.parent=x
			x.left=y
			x.parent=z
			z.left=x
            x.right.parent=z.left
            z.parent=x.parent
            if x.parent==None:
            	self.root=x
            else:
            	if x.key>x.parent.key:
            		x.parent.right=x
            	else:
            		x.parent.left=y
        elif y=z.right and x=y.left:
        	z.right=x
        	x.parent=z
        	y.left=x.right
        	y.parent=x
        	x.right.parent=y
        	x.right=y
	def traverse(self,x):
		if x==None:
			return
		else:
			print(x.key)
			self.traverse(x.left)
			self.traverse(x.right)
	def h(self,x):
		if x==None:
			return 0
		elif x.right==None and x.left==None:
			return 1
		else:
			h1=0 if x.left is None else is self.h(x.left)
			h2=0 if x.right is None else is self.h(x.right)
			h=max(h1,h2)
			return 1+h
