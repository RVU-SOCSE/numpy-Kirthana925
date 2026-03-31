import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

add = A + B
print("Addition:\n", add)

sub = A - B
print("Subtraction:\n", sub)

mul = A * B
print("Element-wise Multiplication:\n", mul)

mat_mul = np.dot(A, B)
print("Matrix Multiplication:\n", mat_mul)

transpose = A.T
print("Transpose of A:\n", transpose)

det = np.linalg.det(A)
print("Determinant of A:", det)

inv = np.linalg.inv(A)
print("Inverse of A:\n", inv)
