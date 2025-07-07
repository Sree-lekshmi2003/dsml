import numpy as np
arr=np.array([[1,2,4],[4,5,6]])
brr=np.array([[1,2,4],[4,5,6]])
print("first array:",arr)
print("second array:",brr)
if np.array_equal(arr,brr):
	print("equals")
else:
	print("not equal")
