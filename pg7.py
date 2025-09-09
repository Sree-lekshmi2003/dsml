import numpy as np
arr=np.array([[2,5,8,10],[3,4,6,9]])
print(arr)
r=np.sum(arr)
print("sum is:",r)
column=np.sum(arr,axis=0)
print("colum  wise sum is:")
print(column)
row=np.sum(arr,axis=1)
print("row wise sum is:")
print(row)

