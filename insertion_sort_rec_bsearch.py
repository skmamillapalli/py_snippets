#!/usr/local/bin/python3
"""Insertion sort runs with a worst-case running time of O(n^2) as n grows. lets see if
an optimization is possible with recursion and usage of b-search to insert next element
in the sorted sub-array"""

import random
import unittest

A = []

def binary_search(A, l, h, ele):
    """Search for an ele and return its index if found. Else return
       the position that the ele can take in the sorted array
       h = index of last_ele + 1 """
    if(l<h):
        mid = (l + h) // 2
        if(A[mid]==ele):
            print("FOUND! Caught him here at position {}.".format(mid))
            pos = mid
        elif(A[mid] > ele):
            pos = binary_search(A, l, mid, ele)
        else:
            pos = binary_search(A, mid+1, h, ele)
        return pos
    else:
        # This is the actual position resolver, happens only when l=h. Note that l > h is not possible 
        # as mid is either decremented towards l or incremented towards h.
        #
        # print(" {} Not found, but can fit in nicely at position {} for array {}.".format(ele, h, A))
        return h

def test_function():
    for _ in range(5):
        arr_size = random.randint(1,10)
        arr = sorted(random.sample(range(50), arr_size))
        ele = random.randint(1,50)
        print("Searching for {} in the array {} of size {}.".format(ele, arr, arr_size))
        binary_search(arr, 0, len(arr), ele)

def insert(A, n):
    """Insert element at A[n] into sub-array A[n-1]"""
    pos = binary_search(A, 0, n, A[n])
    ele = A[n]
    i = n-1
    while i >= pos:
        A[i+1] = A[i]
        i -= 1
    A[pos] = ele

def rec_insertion_sort(A, n):
    """Leverage the modified B_search algorithm defined above to optimize the RT.
       n = Highest index in the array. """
    if n > 0:
        rec_insertion_sort(A, n-1)
        insert(A, n)

class TestInsertionSortWithRecursionBS(unittest.TestCase):
    def test_i_sort_rec_b_search(self):
        for _ in range(500):
            global A
            arr_len = random.randint(10, 100)
            A = random.sample(range(2,1000), arr_len)
            rec_insertion_sort(A, arr_len-1)
            self.assertEqual(A, sorted(A))

# A = [4,1,2,6,14,-2]
# rec_insertion_sort(A, 5)

if __name__ == '__main__':
    unittest.main()

# A function to test B_search funtionality.
# test_function()
