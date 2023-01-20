#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(len(arr)-1,-1,-1):
        k = i-1
        key = arr[i]
        while k >= 0 and key < arr[k]:
            arr[k+1] = arr[k]
            # for elem in arr:
            #     print(elem ,end = " ")
            print(*arr)
            k-=1
        arr[k+1] = key
    print(*arr)
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
