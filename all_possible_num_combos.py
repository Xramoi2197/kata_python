def combos(n, m = 1):
    if n < m:return []
    res = [[n]]
    for i in range(m, n):
        l = [i]
        for j in combos(n - i, i):
           res += [l + j]
    return res


if __name__ == "__main__":
    assert combos(1) == [[1]]
    assert sorted(combos(2)) == [[1, 1], [2]]
    assert sorted(combos(3)) == [[1, 1, 1], [1, 2], [3]]
    assert sorted(combos(4)) == [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]]
