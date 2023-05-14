import numpy as np


def someTest() -> None:
    array1 = np.array([10,20,30])
    print(array1)
    array1_index1 = array1[0]
    print(array1_index1)
    pass

#print("Running some tests with arrays!")
#someTest()


def multiplyTwoArrays() -> None: 
    array1 = np.linspace(1,3,2,dtype=int)
    print(array1)
    array2 = np.linspace(2,3,2,dtype=int).reshape(2,1)
    print(array2)
    array3 = np.matmul(array1,array2)
    print(array3)


multiplyTwoArrays()

