import matplotlib.pyplot as plt
import numpy as np

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]
x = np.array(languages)
y = np.array(popularity)

colors = ['red', 'blue', 'green', 'orange', 'purple', 'black']

plt.barh(x, y, color=colors)

plt.xlabel("Popularity (%)")
plt.ylabel("Programming Languages")
plt.title("Popularity of Programming Languages")

plt.show()

