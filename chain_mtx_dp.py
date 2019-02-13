#python2 filename.py

import sys 

# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n 
def MatrixChainOrder(p, n): 
	# For simplicity of the program, one extra row and one 
	# extra column are allocated in m[][]. 0th row and 0th 
	# column of m[][] are not used 
	m = [[0 for x in range(n)] for x in range(n)] #creating a list of 'n' 0's , 'n' times
												  #which is equivalent to matrix with 5 rows and 5 colums initialized to 0
										  		  #0th row and 0th used for simplicity

	# m[i,j] = Minimum number of scalar multiplications needed 

	# cost is zero when multiplying one matrix. 
	for i in range(1, n): 
		m[i][i] = 0# cost zero for diagonal elements

	 
	for L in range(2, n): # L is chain length.
		for i in range(1, n-L+1): 
			j = i+L-1
			m[i][j] = sys.maxint#assigning infinity 
			for k in range(i, j): 
				q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] #calculating the cost
				if q < m[i][j]: 
					m[i][j] = q #assigning the minimum cost

	return m[1][n-1] 



arr=[]
arr1=0
print 'enter the no:of matrices'
mtrx=input()

for i in range(mtrx+1):
	arr1=input()
	arr.append(arr1)

#arr = [50, 10, 40 ,30 ,5] 
size = len(arr)

print("Minimum number of multiplications is " +
	str(MatrixChainOrder(arr, size))) 

