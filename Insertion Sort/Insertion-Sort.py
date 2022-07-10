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
        current=arr[-1]
        j=n-1
        while j>0 and arr[j-1]>=current:
            arr[j]=arr[j-1]
            print(' '.join(map(str, arr)))
            j-=1
        arr[j]=current
        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
