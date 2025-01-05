#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count = {'pos':0, 'neg':0, 'zero':0}
    visited = []
    for el in arr:
        if el>0:
            count['pos'] = count['pos']+1
        elif el<0:
            count['neg'] = count['neg']+1
        else:
            count['zero'] = count['zero']+1
        
            
    print(count)        
    print(round(count.get('pos')/len(arr), 6))
    print(round(count.get('neg')/len(arr), 6))
    print(round(count.get('zero')/len(arr), 6))
                 
#plusMinus([1,1,0,-1,-1])          
plusMinus([-4, 3, -9, 0, 4, 1]) 

"""if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)"""
