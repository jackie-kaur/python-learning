lst = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def binary_search(s, e, v, lst):
    if s > e:
        return False

    m = (s + e) // 2

    if lst[m] == v:
        return True
    elif lst[m] < v:
        return binary_search(m + 1, e, v, lst)
    elif lst[m] > v:
        return binary_search(s, m - 1, v, lst)

print(binary_search(0, 9, 16, lst))