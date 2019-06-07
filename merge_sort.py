#!/usr/bin/python3
import math
import random
import unittest

def merge(A, l, m, h):
    l1 = m - l + 1
    l2 = h - m
    L1 = list()
    L2 = list()
    # Take dummy arrays
    for i in range(l1):
        L1.append(A[l+i])
    for j in range(l2):
        L2.append(A[j+m+1])
    L1.append(float('inf'))
    L2.append(float('inf'))
    i=0
    j=0
    for k in range(l, h+1):
        if(L1[i] <= L2[j]):
            A[k] = L1[i]
            i+=1
        elif(L1[i] > L2[j]):
            A[k] = L2[j]
            j+=1
    
def merge_sort(A, l, h):
    if (l < h):
        m = (l + h) //2
        merge_sort(A, l, m)
        merge_sort(A, m+1, h)
        merge(A, l, m, h)
    return A

# Do the testing using unittest module
class MergeSortTestCase(unittest.TestCase):
    def test_merge_sort(self):
        for _ in range(1000):
            arr_len = random.choice(range(1,500))
            arr = random.sample(range(1, 5000), arr_len)
            self.assertEqual(sorted(arr), merge_sort(arr,0, arr_len-1))

if __name__ == '__main__':
    unittest.main()
#MergeSortTestCase().test_sort()
#merge([1,8,19, 24,10,23, 25 ],0,3,6)