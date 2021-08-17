import math
import os
import random
import re
import sys


def a_binario(N):
    '''
    Convierte el numero N a binario.
    '''
    return bin(N).replace('0b','')


def contar_consecutivos(B):
    '''
    Cuenta la mayor cantidad de UNOs consecutivos.
    '''
    
    end = len(str(B))
    cont = 0
    maxOnes = 0
    auxB = str(B)

    for idx in range(end-1):

        if auxB[idx] == '1':
            if auxB[idx+1] == '1':
                cont += 1
                if cont > maxOnes:
                    maxOnes = cont
            else:
                cont = 0

    return maxOnes+1




if __name__ == '__main__':
    n = int(input().strip())
    
    B = a_binario(n)
    
    print(contar_consecutivos(B))
