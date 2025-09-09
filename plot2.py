import numpy as np
import matplotlib.pyplot as plt
x=np.array([2,4,6,8,10])
y=np.array([1,3,5,7,9])
x1=np.array([3,5,7,9,11])
y1=np.array([4,5,6,7,8])
plt.plot(x,y,color='red')
plt.plot(x1,y1,color='green')
plt.title('LEGENDS')
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.show()
