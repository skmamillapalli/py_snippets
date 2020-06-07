

#-> Max sub-array problem
#-> Divide and Conquer
#-> O(nlogn)
# Kadane Algorithm, O(n) time


def max_sub_array(A, p, r):
    """Return maximum contiguous array"""
    if p < r:
        q = (p + r) // 2
        l_sum, i1, j1 = max_sub_array(A, p, q)
        r_sum, i2, j2 = max_sub_array(A, q+1, r)
        m_sum, i3, j3 = max_crossover_sub_array(A, p, q, r)
        max_sum = l_sum
        max_l_index = i1
        max_r_index = j1
        if r_sum > max_sum:
            max_sum = r_sum
            max_l_index, max_r_index = i2, j2
        if m_sum > max_sum:
            max_sum = m_sum
            max_l_index, max_r_index = i3, j3
        return max_sum, max_l_index, max_r_index
    return A[p], p, r

def max_crossover_sub_array(A, p, q, r):
    """Return tuple sum, l, r for maximum crossing sub-array"""
    l_max_sum = -999999
    r_max_sum = l_max_sum
    l_sum = 0
    r_sum = 0
    l_index = q
    r_index = q+1
    for i in range(q, p-1, -1):
        l_sum = A[i] + l_sum
        if l_sum > l_max_sum:
            l_max_sum = l_sum
            l_index = i
    for j in range(q+1, r, 1):
        r_sum = A[j] + r_sum
        if r_sum > r_max_sum:
            r_max_sum = r_sum
            r_index = j
    return l_max_sum+r_max_sum, l_index, r_index