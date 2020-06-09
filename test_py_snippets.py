import pytest, nbitadd, maxsubarray
import random, quick_sort
@pytest.mark.parametrize('a, b', [(20,30), (40, 50), (-10, 15)])
def test_n_bit_addition(a, b):
    expected = a + b
    s = nbitadd.n_bit_addition(a, b)
    assert s == expected

@pytest.mark.parametrize('A, p, r', [[[-2, 1, -3, 4, -1, 2, 1, -5, 4], 0, 8]])
def test_max_sub_array_d_and_c(A, p, r):
    expected = (6, 3, 6)
    s = maxsubarray.max_sub_array(A, p, r)
    assert expected == s

# @pytest.mark.parametrize('A, p, r', [[[-2, 1, -3, 4, -1, 2, 1, -5, 4], 0, 8]])
# def test_partition(A, p, r):
#     expected = sorted(A).index(a[i])

