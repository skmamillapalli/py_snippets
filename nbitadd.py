#!/usr/local/bin/python3
import unittest
from collections import deque


def n_bit_addition(A, B):
    """Compute n-bit additions for two n-bit arrays and return
       the computed sum
        A   B    C(i)      S    C(i+1)
        1 + 1    0/1   =   0/1  1/1
        0 + 0    0/1   =   0/1  0/0
        0 + 1    0/1   =   1/0  0/1
        1 + 0    0/1   =   1/0  0/1
    """
    A = bin(A)
    B = bin(B)
    Cr = 0
    A = A.replace('0b', '')
    B = B.replace('0b', '')
    if len(A)!= len(B):
           # do some corrections
           if len(A) < len(B):
               A = '0'*(len(B) - len(A)) + A
           else:
               B = '0'*(len(A) - len(B)) + B
    C = deque()
    print(A, B, C, Cr)
    for i in range(len(A)-1, -1, -1):
        if A[i] == B[i]:
            C.appendleft(str(Cr))
            Cr = A[i] # A or B, doesn't matter
        else:
            C.appendleft(str(1-int(Cr)))
    C.appendleft(Cr)
    return(int(''.join(x for x in C), 2))


    
    
           
