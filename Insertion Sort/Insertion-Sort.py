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
        
        current = arr[-1]
    
        for index in range(len(arr)-2, -1, -1):
            if arr[index] > current:
                arr[index+1] = arr[index]
                print(*arr)
            else:
                arr[index+1] = current
                print(*arr)
                break
        if arr[0] > current:
            arr[0] = current
            print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
