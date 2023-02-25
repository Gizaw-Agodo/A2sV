import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):
    # Write your code here
    prefixSum = [0]*(n+1)
    
    for query in queries:
        start,end ,val = query
        prefixSum[start-1] += val 
        prefixSum[end] -= val
        
    for i in range(1,len(prefixSum)):
        prefixSum[i] += prefixSum[i-1]

    return max(prefixSum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
