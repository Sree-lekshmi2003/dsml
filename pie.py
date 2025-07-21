import matplotlib.pyplot as plt
import numpy as np
x =np.array(['Java','Python','PHP','JavaScript','C#','C++'])
y = np.array([22.2, 17.6, 8.8, 8.0, 7.7, 6.7])
plt.pie(y, labels=x)
plt.xlabel("Programming Languages")
plt.ylabel("Popularity ")
plt.title("pie chart")

plt.show()
