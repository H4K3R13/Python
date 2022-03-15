import numpy as np
import sys
print("Matrix Calculator:\n")
print("\nEnter Matrix 1\n")  
R = int(input("Enter the number of rows:"))
C = int(input("\nEnter the number of columns:"))

matrix1 = []
print("\nEnter the entries rowwise:")
  

for i in range(R): 
    a =[]
    for j in range(C):     
         a.append(int(input()))
    matrix1.append(a)

print("\n Enter Matrix 2")  
M = int(input("\nEnter the number of rows:"))
N = int(input("\nEnter the number of columns:"))

if (C!=M): sys.exit("\nERROR!!! The number column of Matrix 1 is not equal to number of rows of Matrix 2")

matrix2 = []
print("\nEnter the entries rowwise:")
  
for i in range(M):          
    a =[]
    for j in range(N):     
         a.append(int(input()))
    matrix2.append(a)
  
print("\nMatrix 1\n")
for i in range(R):
    for j in range(C):
        print(matrix1[i][j], end = " ")
    print()  

print("\nMatrix 2\n")
for i in range(M):
    for j in range(N):
        print(matrix2[i][j], end = " ")
    print()


print("Multiplication of Matrix 1 and Matrix 2 :\n",np.dot(matrix1,matrix2))