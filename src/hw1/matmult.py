#this is the matrix mult program
import sys

mat1=[] #use this for first matrix to be multiplied
mat2=[] #use this for the second matrix to be multiplied
matfin=[] #final matrix
def create(row,col,mat):
	for i in range(row):
		mat.append([])
		for j in range(col):
			mat[i].append(0.0)

def load(row,col,line,mat):
	#must load when row = 0 outside of this function
	for j in range(col):
		hold=float(line.split(" ")[j])
		#print("hold is : ",hold)
		mat[row][j]=hold

def multiply(mat1,mat2,r1,r2,c1,c2):
	#mult function --> might have to add 1 to final range value
	for a in range(len(mat1)):
		for b in range(len(mat2[0])):
			for c in range(len(mat2)):
				matfin[a][b]+=mat1[a][c]*mat2[c][b]
	

def printy(row,col,mat):
	for j in range(row):
		for t in range(col):
			print(mat[j][t],end=" ")
		print()

r1=0
c1=0
r2=0
c2=0
 #use as line counter
l=0
for line in sys.stdin:
	if l==0 or l==1+r1:
		if(l==0):
			r1=(int)(line.split(" ")[0])
			c1=(int)(line.split(" ")[1])
			l+=1
			create(r1,c1,mat1)
		elif(l==1+r1):
			r2=(int)(line.split(" ")[0])
			c2=(int)(line.split(" ")[1])
			l+=1
			if c1!=r2:
				print("invalid input")
			create(r2,c2,mat2)
	else:
		if l<1+r1:
		#means mat1
			temp=l-1#temporary row number
			for i in range(c1+1):
				load(temp,i,line,mat1)
			l+=1
		elif l>1+r1:
		#means mat2
		#load function here too 
			temp1=l-r1-2
			for v in range(c2+1):
				load(temp1,v,line,mat2)
			l+=1
	
create(r1,c2,matfin)
multiply(mat1,mat2,r1,r2,c1,c2)
#below is printing first, second, and final matrix

#print("mat fin")
if(c1==r2):
	printy(r1,c2,matfin)
