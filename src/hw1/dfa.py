import sys

endCount=4
lineCount=0
endRules=False
states=[]
symbols=[]
starts=None
finals=[]

class Node:
	def __init__(self,start,trans,path,nextNode=None):
		self.start=start
		self.trans=trans
		self.path=path
		self.next=nextNode

class LinkedList:
	def __init__(self):
		self.head=None
		self.size=0

	def add(self,start,trans,path):
		newNode=Node(start,trans,path,self.head)
		self.head=newNode
		self.size+=1
		return True
	
	def printy(self):
		curr=self.head
		while curr:
			print("start: ",curr.start," next state: ",curr.trans," path taken: ",curr.path)
			curr=curr.next

def isValidEl(currState,l):
	#takes the current state and checks if it's in the states list)
	#where curr State is to be checked and states is the list
	x=0
	while(x<len(l)):
		#print(l[x])
		if(l[x].strip('\n')!=currState.strip('\n')):
			#print("_____comparing______")
			#print(l[x]," ",currState)
			x+=1	
		else:
			#print("equal")
			return True
	return False
			

diana=LinkedList()


for line in sys.stdin:
	term=line.split(" ")[0]
	lineCount+=1
	
	while(lineCount>=4 and endRules==False and (term.strip('\n')!="end_rules")):
		endCount+=1
		#print("____we are in rules_____")
		
			#means this is the first rule
		startState=line.split(" ")[0]
		transState=line.split(" ")[2]
		lineTaken=line.split(" ")[4]
		diana.add(startState,transState,lineTaken)
	
		#print(startState," ",transState," ",lineTaken,end=" ")
		break
		
	if(term=="states:"and endRules==False):
		#print("______states______")
		term=line.replace('states: ','')
		states=term.split()
		#print(states)
	elif(term=="symbols:" and endRules==False):
		#print("___symbols___")
		term=line.replace('symbols: ','')
		symbols=term.split()
		#print(symbols)
		#print()
		#means begin rule
		#a method to create the dictionary
	elif(term.strip('\n')=="end_rules"):
		#print("___end rules___")
		endRules=True
	elif(endRules==True):		
		if(term=="start:"):
		#	print("____start____")
			#can there be more than one start? on piazza
			term=line.replace('start: ','')
			starts=term.split(" ")[0]
			#print(starts)
		#do this
		elif(term=="final:"):
		#do this
			#print("____final____")
			term=line.replace('final: ','')
			finals=term.split()
			#print(finals)
		else:
		#means this is where we input. Must run input against dictionary
		#	print(term,end=" ")
			#print("____inputs_____")
		
			#print(line)
							
			#first, take each symbol in the word
			x=0
			currentState=starts.strip('\n')
			isFound=False
			if(isValidEl(currentState,states)is False):
				#checks first state only
				print("rejected")
				break
			charCount=0
			#print("start state is : ",starts)
			for x in range(len(line)-1):
				curChar=line[x]
				charCount+=1
				isFound=False
				#first, check if valid symbol
				#print("looking at char #",charCount," : ",curChar," at current state: ",currentState)	
				if (isValidEl(curChar,symbols)):
					#iterate through rules to find start state that matches current state and path that matches curr.path
					curr=diana.head
					
					while curr:
						#print("current node's start is : ",curr.start," and path is : ",curr.path)
						#print("__________________________________________________________________")
						nodeStart=curr.start.strip('\n')
						nodePath=curr.path.strip('\n')
						nodeTrans=curr.trans.strip('\n')
						if(currentState==nodeStart and curChar==nodePath):
							#print("rule match")
							currentState=nodeTrans
							if(isValidEl(nodeTrans,states)is False):#if it doesn't work, take this block out
								print("rejected")
								break
							isFound=True
							#print()
							break
						else:
							curr=curr.next
					#print("length of ",line," : ",len(line)-1)#why is this saying it's 5?
					if (isFound is True and charCount==(len(line)-1)):
						if(isValidEl(currentState,finals)):
							print("accepted")
							break
						else:
							print("rejected")
							break
					elif(isFound is True and charCount!=len(line)):
						continue
					elif(isFound is False):
						print("rejected")
						break
					#if we break out of linked list --> means we didn't find what we're looking for
					#if(isFound is False):
					#	print("rejected")
					#elif(isFound is True and charCount==len(line)):
					#	#means last element
					#	if(isValidEl(currentState,finals)):
					#		#means valid final state
					#		print("accepted")
				else:
					#means invalid
					print("rejected")	
					break
					
										
						
			
#print("_______rules in linked list________")
#diana.printy()




