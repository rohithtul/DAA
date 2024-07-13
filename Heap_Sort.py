import time
import numpy as np
import math

def heap_sort(x):
    build_max_heap(x)
    for i in range(len(x)-1, 0, -1):
        c = x[0]
        x[0] = x[i]
        x[i] = c
        max_heapify(x, i, 0)

def build_max_heap(x):
    for i in range((len(x)//2)-1, -1, -1):
        max_heapify(x, ar_heapsize, i)


def max_heapify(x, ar_heapsize, i):
    l = 2*i + 1
    r = 2*i + 2
    if(l < ar_heapsize and x[l] > x[i]):
        largest = l

    else:
        largest = i

    if(r < ar_heapsize and x[r] > x[largest]):
        largest = r

    if(largest != i):
        d = x[i]
        x[i] = x[largest]
        x[largest] = d
        max_heapify(x, ar_heapsize, largest)            


if __name__ == '__main__':
  n = int(input("Number of elements: "))
  x = []
  y = []
  #if the input array is reverse sorted
  for j in range(n, 0, -1):
      y.append(j)
  ar_heapsize = len(y)      
  print("Reverse order input array: \n ",y)
  start_time = time.time() * 1000
  #print("start time :" + str(start_time))
  heap_sort(y)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time))
  print("Sorted Array: ")
  print(y)
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")
  
  
  #if the input array is sorted
  for i in range(1,n+1):
      x.append(i)
  ar_heapsize = len(x) 
  print("Sorted order input array: \n ",x)
  start_time = time.time() * 1000
  #print("start time :" + str(start_time))
  heap_sort(x)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time))
  print("Sorted Array: ")
  print(x)
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")
  
  
  #if the input array is random
  np.random.seed(seed=2)
  z = np.random.randint(1, 100000, n)
  ar_heapsize = len(z)
  print("Random input array: \n ",z)
  start_time = time.time() * 1000
  #print("start time :" + str(start_time))
  heap_sort(z)
  end_time = time.time() * 1000
  #print("end time :" + str(end_time))
  print("Sorted Array: ")
  print(z)
  total_time = end_time - start_time
  print("Execution time: ", str(total_time), " milli seconds")

    
  
