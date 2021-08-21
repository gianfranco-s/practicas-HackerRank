#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))

    
    # a = [4,3,1,2]
    # a = [1,2,3]
    a = [3,2,1]
    n = len(a)
    totalSwaps = 0
    for i in range(n):
        # Track number of elements swapped during a single array traversal
        numberOfSwaps = 0;

        for j in range(n-1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numberOfSwaps += 1
        # print(numberOfSwaps)                
        totalSwaps += numberOfSwaps        
        
        if numberOfSwaps == 0:
            # If no elements were swapped during a traversal, array is sorted
            break
    
    # Diferentes maneras de hacer print con datos:
        
    # Usando f'Cadena {dato}'
    # print(f'Array is sorted in {totalSwaps} swaps.')
    
    # Usando 'Cadena {dato}'
    # print('First Element: {}'.format( a[0] ))
    
    # Usando print únicamente
    # print('Last Element: ',a[-1])

    # Hay oootros métodos más

    # para que lo agarre HackerRank:
    output1 = f'Array is sorted in {totalSwaps} swaps.'
    output2 = f'First Element: {a[0]}'
    output3 = f'Last Element: {a[-1]}'
    print(output1)
    print(output2)
    print(output3)
    
    