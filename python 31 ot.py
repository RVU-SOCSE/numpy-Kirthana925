Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============= RESTART: C:/Users/HP/Documents/python 31/python 31.py ============
Matrix A:
 [[1 2]
 [3 4]]
Matrix B:
 [[5 6]
 [7 8]]
Addition:
 [[ 6  8]
 [10 12]]
Subtraction:
 [[-4 -4]
 [-4 -4]]
Element-wise Multiplication:
 [[ 5 12]
 [21 32]]
Matrix Multiplication:
 [[19 22]
 [43 50]]
Transpose of A:
 [[1 3]
 [2 4]]
Determinant of A: -2.0000000000000004
Inverse of A:
 [[-2.   1. ]
 [ 1.5 -0.5]]

================== RESTART: C:/Users/HP/Documents/python 32.py =================
1D Array: [1 2 3 4]
2D Array:
 [[1 2]
 [3 4]]
Zeros:
 [[0. 0. 0.]
 [0. 0. 0.]]
Ones:
 [[1. 1.]
 [1. 1.]]
Identity:
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
Shape: (2, 2)
Size: 4
Data type: int64
Reshaped array:
 [[1 2]
 [3 4]]
First element: 1
Slice: [2 3]

=== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python314/python 33.py ==
Original Data:
          Name   Age  Marks
0    Kirthana  19.0   85.0
1     Koushik   NaN   90.0
2  Prathiksha  24.0    NaN
3    Prashant   NaN   90.0
4         NaN  18.0   88.0

After Filling Missing Values:
          Name        Age  Marks
0    Kirthana  19.000000  85.00
1     Koushik  20.333333  90.00
2  Prathiksha  24.000000  88.25
3    Prashant  20.333333  90.00
4     Unknown  18.000000  88.00

After Dropping Missing Values:
        Name   Age  Marks
0  Kirthana  19.0   85.0

After Removing Duplicates:
          Name        Age  Marks
0    Kirthana  19.000000  85.00
1     Koushik  20.333333  90.00
2  Prathiksha  24.000000  88.25
3    Prashant  20.333333  90.00
4     Unknown  18.000000  88.00
>>> 
== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python314/p-ython 34.py ==
Original Data:
          Name   Age  Marks
0    Kirthana  20.0   85.0
1     Koushik   NaN   90.0
2  Prathiksha  19.0    NaN
3    Prashant   NaN   90.0
4         NaN  22.0   88.0

After Filling Missing Values:
          Name        Age  Marks
0    Kirthana  20.000000  85.00
1     Koushik  20.333333  90.00
2  Prathiksha  19.000000  88.25
3    Prashant  20.333333  90.00
4     Unknown  22.000000  88.00

After Dropping Missing Values:
        Name   Age  Marks
0  Kirthana  20.0   85.0

After Removing Duplicates:
          Name        Age  Marks
0    Kirthana  20.000000  85.00
1     Koushik  20.333333  90.00
2  Prathiksha  19.000000  88.25
3    Prashant  20.333333  90.00
4     Unknown  22.000000  88.00
