import numpy as np
A = np.array([[4,-2,4,2],[-2,10,-2,-7],[4,-2,8,4],[2,-7,4,7]])
print (A)
for i in range (4):
	for k in range(0, i):
		A[i,i] -= (A[k,i] * A[k,i])
	if A[i,i] <= 0 : print( "A is not +ve definite" )
	A[i,i] = np.sqrt(A[i,i])
	for j in range(i+1, 4):
		for k in range(0, i):
			A[i,j] -= (A[k,i] * A[k,j])
		A[i,j] = A[i,j]/A[i,i]
		
print ("After Cholesky Factorization")
print (A)

for i in range(4):
	for j in range(i+1, 4):
		A[j,i] = 0
print ("\n", A)

B = np.array([[4,-2,4,2],[-2,10,-2,-7],[4,-2,8,4],[2,-7,4,7]])
print (B)
for i in range (4):
	for k in range(0, i):
		B[i,i] -= (B[i,k] * B[i,k])
	if B[i,i] <= 0 : print ( "A is not +ve definite")
	B[i,i] = np.sqrt(B[i,i])
	for j in range(i+1, 4):
		for k in range(0, i):
			B[j,i] -= (B[i,k] * B[j,k])
		B[j,i] = B[j,i]/B[i,i]
		
print ("After Cholesky Factorization")
print (B)

for i in range(4):
	for j in range(i+1, 4):
		B[i,j] = 0
print ("\n", B)