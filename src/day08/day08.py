#import numpy as np
#a = np.array([[1,2,3],[4,5,6]])
#b = np.array([10,20,30])
#result = a+b
#print(result)
 
import numpy as np
one_d=np.array([1,2,3,4,5,6,7])
print(one_d)

two_d=np.array([[1,2,3],[5,6,7]])
print(two_d)

three_d=np.array([[3,2,1],[4,5,3],[7,6,7]])
print(three_d)


#vectorization vs loop example
arr = np.random.rand(100)

squared = arr**2
print(squared[0:30])

#array manipulation
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)
hstacked = np.hstack((a, b))
print(hstacked)

#statistical functions
data = np.array([[10, 20, 30],[40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))


#linear algebra
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(np.dot(A,B))



print("task-1,normalizer")
import numpy as np
scores = np.random.randint(50,101,size=(5,3))
subject_mean =scores.mean(axis=0)
centered_score = scores-subject_mean
print("original scores:\n",scores)
print("\nsubject-wise mean:\n",subject_mean)
print("\ncentered scores(after broadcasting):\n",centered_score)



















print("task-2,the reshaper")
import numpy as np
data =np.arange(24)
reshaped_data = data.reshape(4,3,2)
final_data = reshaped_data.transpose(0,2,1)
print("Final Shape:", final_data.shape)
print("Final Array:\n", final_data)

















