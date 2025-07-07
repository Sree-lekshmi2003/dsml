import numpy as np
arr=np.array([[1,2,4],[5,6,7]])
print("array elements:")
print(arr)
r=np.sum(arr)
print("sum is:",r)
column=np.sum(arr,axis=0)
print("colum  wise sum is:")
print(column)
row=np.sum(arr,axis=1)
print("row wise sum is:")
print(row)

