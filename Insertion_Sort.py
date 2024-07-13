import time
import numpy as np
import math


def insertion_sort(ar):
    x = []
    for i in (ar):
        x.append(i)
    
    #print(x)
    #print(len(x))
    for j in range(1,len(x)):
        key = x[j]
        i = j-1
        while(i>=0 and x[i] > key):
            x[i+1] = x[i]
            i = i - 1
        x[i+1] = key

    print("Sorted Array: ")
    print(x)

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
  insertion_sort(y)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time))
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")
  
  
  #if the inout array is sorted
  for i in range(1,n+1):
      x.append(i)
   
  print("Sorted order input array: \n ",x)
  start_time = time.time() * 1000
  #print("start time :" + str(start_time))
  insertion_sort(x)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time)
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")
  
  
  #if the input array is random
  np.random.seed(seed=2)
  z = np.random.randint(1, 100000, n)
  print("Random input array: \n ",z)
  start_time = time.time() * 1000
  #print("start time :" + str(start_time))
  insertion_sort(z)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time))
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")
        