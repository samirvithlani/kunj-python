import numpy as np
#random num array...
x = np.random.rand(3,2)
#print(x)
x = np.random.randn(2,3)
#print(x)
#x = np.random.randint(1,10,5)
np.random.seed(42)
x = np.random.randint(1,10,(3,3))
print(x)
x = np.random.choice([100,20,34,56,78,90])
#print(x)