import time
import numpy as np
import math


#print(x[3])
def partition(x, p, r):
    pivot = x[r]
    j = p - 1
    for k in range(p, r):
        if x[k] <= pivot:
            j = j + 1
            arr = x[j]
            x[j] = x[k]
            x[k] = arr
        
    var1 = x[j+1]
    x[j+1] = x[r]
    x[r] = var1
    return j+1

def quicksort(x, p, r):
    if(p<r):
        pr = partition(x, p, r)
        quicksort(x, p, pr-1)
        quicksort(x, pr+1, r)
        
        

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
  quicksort(y, 0, n - 1)
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
  quicksort(x, 0, n - 1)
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
  quicksort(z, 0, n - 1)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time))
  print("Sorted Array: ")
  print(z)
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")
