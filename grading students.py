#!/bin/python

import math
import os
import random
import re
import sys

# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

n = int(input())
for a0 in range(n):
    grade = int(input())
    if grade >= 38:
        mod5 = grade % 5
        if mod5 >= 3:
            grade = grade + (5 - mod5)
    print(grade)



    
