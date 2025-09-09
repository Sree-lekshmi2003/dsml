import numpy as np
import matplotlib.pyplot as plt
x=np.array(['Java','Python','PHP','JavaScript','c#','c++'])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
plt.bar(x,y)
plt.title('BAR CHART')
plt.xlabel('Programming  language')
plt.ylabel('popularity')
plt.show()
