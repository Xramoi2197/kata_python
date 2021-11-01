"""
https://www.codewars.com/kata/52f677797c461daaf7000740/solutions/python
best:
from fractions import gcd
from functools import reduce

def solution(a):
    return reduce(gcd, a) * len(a)

second:
def solution(a):
    a_len = len(a)
    a = set(a)
    while len(a) != 1:
        b = max(a)
        a.remove(b)
        a.add(b-max(a))
    return(max(a) * a_len)
"""


def solution(a):
    st = set(a)
    while min(st) != max(st):
        mx = max(st)
        mn = min(st)
        st -= {mx}
        for num in st:
            if mx <= mn:
                break
            elif num < mx:
                mx = mx - num
        if mx != mn:
            st.add(mx)
    return st.pop() * len(a)


if __name__ == "__main__":
    assert solution([9]) == 9
    assert solution([6, 9, 21]) == 9
    assert solution([1, 21, 55]) == 3
