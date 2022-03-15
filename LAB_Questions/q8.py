import numpy as np
m = np.array([[1, 2],[2, 3]])
print("Printing the given square array:\n",m)
w, v = np.linalg.eig(m)
d=np.linalg.det(m) 
print("Printing the Eigen values of the given square array:\n",w)
print("Printing Right eigenvectors of the given square array:\n",v)
print("Printing Determinant of the given square array:\n",d)