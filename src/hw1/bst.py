import sys

class Node:
	def __init__ (self,data):	
		self.data=data
		self.left=None
		self.right=None
		self.size=0

	def printy(self):
			ptr=self
			if(ptr is not None):
				print("(",end=" ")
				if(ptr.left is not None):
					ptr.left.printy()
				print(ptr.data, end=" ")
				if ptr.right is not None:
					ptr.right.printy()
				print(")",end=" ")		
	
	def query(self,data):
		if(self.data is None or self.size==0):
			print("not found")
			return False
		elif(self.data==data):
			print("found: root")
			return True
		elif(self.data !=data and self.right is None and self.left is None):
			print("not found")
			return False
		else:
			#print("searching for: ",data)
			word=""
			ptr=self
			#isFound=False
			while(ptr is not None):
				#print("data in current node: ",ptr.data)
				if(ptr.data==data):
					#print("node data : ",ptr.data)	
					print("found:",word)
					return True
				elif(ptr.data<data):
					ptr=ptr.right
					word+="r "
				else:
					ptr=ptr.left
					word+="l "
			#end of while loop
			print("not found")

	def insert(self,data):
		if(self.data is None):
			#print("empty tree")
				self.data=data
				self.size+=1
		else:
			#means at least one element in bst
			if(self.data == data):
				return True
			elif(self.data !=data and self.right is None and self.left is None and self.size==1):
					if(data>self.data):
						self.right=Node(data)
						self.size+=1
					else:
						self.left=Node(data)
						self.size+=1
			else:
				ptr=self
				prev=ptr
				while(ptr is not None):
					if(ptr.data == data):
						#print("already exists in tree!")
						return True
					elif(data>ptr.data):
						prev=ptr
						ptr=ptr.right
					else:
						prev=ptr
						ptr=ptr.left
				#if we break out, means we reached None
				if(data<prev.data):
					prev.left=Node(data)
					self.size+=1
				else:
					prev.right=Node(data)
					self.size+=1
	
root=Node(None)				
for line in sys.stdin:
	t=(int)(line.split(" ")[1])
	c=(line.split(" ")[0])
	
	if(c=="i"):
		root.insert(t)
	elif(c=="q"):
		root.query(t)
#root.printy()
#print()
