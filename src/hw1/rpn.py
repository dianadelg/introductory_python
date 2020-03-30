import sys
class Node:
	def __init__(self,data,nextNode=None):
		self.data=data
		self.next=nextNode
		
	def getData(self):
		return self.data

	def setData(self,val):
		self.data=val
	
	def getNextNode(self):
		return self.next

	def setNextNode(self,val):
		self.next=val

class LinkedList:
	def __init__(self):
		self.head=None
		self.size=0

	def getSize(self):
		return self.size

	def push(self,data):
		newNode=Node(data,self.head)
		self.head=newNode
		self.size+=1
		return True

	def pop(self):
		if(self.size!=0):
			temp=self.head.data
			self.head=self.head.next
			self.size-=1
			return temp
		#else:
			#print("invalid operation")

	def printNode(self):
		curr=self.head
		while curr:
			print(curr.data,end=" ")
			curr=curr.getNextNode()

def isNum(op):
	if(op=="+" or op=="-" or op =="/" or op =="*" or op=="~"):
		return False
	else:
		return True

diana=LinkedList()
for line in sys.stdin:
	op=line.split(" ")[0]
	op=op.strip('\n')
	#print(op)
	
	#if(op=="/"):
	#	print("division")
	
	if(op=="+" or op =="-" or op == "*" or op =="/"):
	#	print("OPERATION IS IN THE FIRST CONDITIONAL")
		if(diana.size==0 or diana.size==1):
			print("invalid operation")
			#continue
			#might need to be removed
		else:
			op1=diana.pop()
			op2=diana.pop()
			if(op=="+"):
				if(isNum(op1) and isNum(op2)):
					temp=(float)(op2+op1)
					print(temp)
					diana.push(temp)
				else:
					#means one of them is a operator and this causes issues
					print("invalid operation")
					diana.push(op2)
					diana.push(op1)

			elif(op=="-"):
				if(isNum(op1)and isNum(op2)):
					temp=(float)(op2-op1)
					print(temp)
					diana.push(temp)
				else:
					#same as above
					print("invalid operation")
					diana.push(op2)
					diana.push(op1)
			elif(op=="*"):
				if(isNum(op1)and isNum(op2)):
					temp=(float)(op2*op1)
					print(temp)
					diana.push(temp)
				else:
					print("invalid operation")
					diana.push(op2)
					diana.push(op1)
			else:
				#division
				if(isNum(op1)and isNum(op2)):
					if(op1!=0):
						temp=(float)(op2/op1)
						print(temp)
						diana.push(temp)
					else:
						#means division by 0 -- check this
						diana.push(op2)
						diana.push(op1)
				else:
					print("invalid operation")
					diana.push(op2)
					diana.push(op1)
					#means both numbers
	elif(op=="~"):
		if(diana.size==0):
			print("invalid operation")
		else:
			hold=diana.pop()
			if(isNum(hold)):
				temp=(float)(0-hold)
				print(temp)
				diana.push(temp)
			else:
				print("invalid operation")
				diana.push(hold)
	elif(isNum(op)):
		#means it's a number
		temp=(float)(line.strip('\n'))
		diana.push(temp)
		print(temp)
