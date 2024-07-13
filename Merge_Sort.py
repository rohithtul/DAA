import time
import numpy as np
import math

def merge(A, p, q, r):
    L = []
    R = []
    L = A[p: q+1]
    R = A[q+1:r+1]
    L = np.append(L, np.inf)
    R = np.append(R, np.inf)
    i=0
    j=0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = int(L[i])
            i = i + 1
        else:
            A[k] = int(R[j])
            j = j + 1

def mergesort(A, p, r):
    if(p<r):
        q = math.floor((p+r)//2)
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)
        
        
if __name__ == '__main__':
  n = int(input("Number of elements: "))
  x = []
  y = []
  #if the input array is reverse sorted
  for j in range(n, 0, -1):
      y.append(j)
  print("Reverse order input array: \n ",y)
  start_time = time.time() * 1000
  #print("start time :" + str(start_time))
  mergesort(y, 0, n - 1)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time))
  print("Sorted Array: ")
  print(y)
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")
  
  
  #if the inout array is sorted
  for i in range(1,n+1):
      x.append(i)
   
  print("Sorted order input array: \n ",x)
  start_time = time.time() * 1000
  #print("start time :" + str(start_time))
  mergesort(x, 0, n - 1)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time))
  print("Sorted Array: ")
  print(x)
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")
  
  
  #if the input array is random
  np.random.seed(seed=2)
  z = np.random.randint(1, 100000, n)
  print("Random input array: \n ",z)
  start_time = time.time() * 1000
  #print("start time :" + str(start_time))
  mergesort(z, 0, n - 1)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time))
  print("Sorted Array: ")
  print(z)
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")
