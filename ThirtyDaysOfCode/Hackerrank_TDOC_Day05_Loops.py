#!/bin/python3

import math
import os
import random
import re
import sys

def multiplicar(N):
    for cont in range(10):
        
        print(f"{N} x {cont+1} = {N*(cont+1)}")


if __name__ == '__main__':
    n = int(input().strip())
    multiplicar(n)
