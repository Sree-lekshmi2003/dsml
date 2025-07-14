import numpy as np

print("enter the elements:")
a=input("enter first element:")
b=input("enter second elemet:")
c=input("enter third element:")
d=input("enter fourth number:")
s=np.array([[int (a),int (b)],[int (c),int (d)]])
print(s)
invers=np.linalg.inv(s)
print(invers)
