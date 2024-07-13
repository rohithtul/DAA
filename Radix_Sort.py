import time
import numpy as np
import math

def countingSort(arr, exp1):
    n = len(arr)

    B = [0] * (n)

    C = [0] * (10)

    for i in range(0, n):
        index = arr[i] // exp1
        C[index % 10] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n-1, -1, -1):
        index = arr[i] // exp1
        B[C[index % 10] - 1] = arr[i]
        C[index % 10] -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = B[i]


def radixSort(arr):

    max1 = max(arr)

    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10


if __name__ == '__main__':
    n = int(input("Number of elements: "))
    x = []
    y = []
    # if the input array is reverse sorted
    for j in range(n, 0, -1):
        y.append(j)
    print("Reverse order input array: \n ", y)
    start_time = time.time() * 1000
    #print("start time :" + str(start_time))
    radixSort(y)
    end_time = time.time() * 1000
    #print("end time :" + str(end_time))
    print("Sorted Array: ")
    print(y)
    total_time = end_time - start_time
    print("Execution time of worst case: ", str(total_time), " milli seconds")

    # if the inout array is sorted
    for i in range(1, n + 1):
        x.append(i)

    print("Sorted order input array: \n ", x)
    start_time = time.time() * 1000
    #print("start time :" + str(start_time))
    radixSort(x)
    end_time = time.time() * 1000
    #print("end time :" + str(end_time))
    print("Sorted Array: ")
    print(x)
    total_time = end_time - start_time
    print("Execution time of best case: ", str(total_time), " milli seconds")

    # if the input array is random
    np.random.seed(seed=2)
    z = np.random.randint(1, 100000, n)
    print("Random input array: \n ", z)
    start_time = time.time() * 1000
    #print("start time :" + str(start_time))
    radixSort(z)
    end_time = time.time() * 1000
    #print("end time :" + str(end_time))
    print("Sorted Array: ")
    print(z)
    total_time = end_time - start_time
    print("Execution time of random: ", str(total_time), " milli seconds")