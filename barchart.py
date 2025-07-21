import matplotlib.pyplot as plt
import numpy as np
languages =np.array(['Java','Python','PHP','JavaScript','C#','C++'])
popularity = np.array([22.2, 17.6, 8.8, 8.0, 7.7, 6.7])


plt.bar(languages, popularity, color='skyblue')
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")

plt.show()
