#!/bin/bash/env python
import random
"""Quick sort is a better performing sort, given the low constant factor and better average running case of thetad(nlogon)
   It does however, gets to O(n^2) as its overall running time, given it gets to the recurrence of the form
   T(n) = T(n-1) + O(n) for array with elements in descending/ascending order."""

#4 2 6 8 (0, 3)
def partition(A, p, r):
    """Take A as input. Choose a pivot, and arrange array such that all elements left of pivot are <= pivot
        and elements right of pivot are >= pivot."""
    pivot = A[r]
    k = p-1 # Represents an array with elements <= pivot. Initially no such elements. Grows from left.
    for i in range(p, r):
        if A[i] < pivot:
            #Increment k, we have an candidate for left array
            k += 1
            A[k], A[i] = A[i], A[k]
    A[k+1], A[r] = A[r], A[k+1]
    return k+1

def quick_sort(A, p, r):
    if p < r:
        # Divide part is not strightforward, Run partition algorithm
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        print(q,r)
        quick_sort(A, q+1, r)

A = random.sample(range(1,100), 10)
print(A)
quick_sort(A, 0, 9)
print(A)