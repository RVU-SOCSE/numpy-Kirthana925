import numpy as np


arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2], [3, 4]])      

print("1D Array:", arr1)
print("2D Array:\n", arr2)


zeros = np.zeros((2, 3))                   
ones = np.ones((2, 2))                    
identity = np.eye(3)                      

print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Identity:\n", identity)


print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data type:", arr2.dtype)


reshaped = arr1.reshape(2, 2)
print("Reshaped array:\n", reshaped)


print("First element:", arr1[0])
print("Slice:", arr1[1:3])
