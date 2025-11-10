import numpy as np

x = np.array([1,2,3,4,5])    
print(x)
x = np.array([[1,2,3],[4,5,6]],dtype="float")
print(x)

#from existing data
a = np.arange(0,10,2)
print(a)
a = np.linspace(0,2,5)
print(a)
a = np.logspace(1,4,3)
print(a)

a = np.zeros((3,3))
print(a)

a = np.ones((4,3))
print(a)

a = np.eye(3)
print(a)

a = np.full((2,2),9)
print(a)

a = np.empty((3,3))
print(a)

a = np.arange(10).reshape(5,2)
print(a)


