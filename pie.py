import numpy as np
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','c#','c++']
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
plt.pie(y,labels=x)
plt.title('PIE CHART')
plt.show()

