import time

lst = [320, 98, 366, 250, 55, 336, 37]

def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst

def linear_search(num):
    for l in lst:
        if l == num:
            return True
    return False

def binary_search(s, e, v, lst):
    if s > e :
        return False
    
    m = (s + e) // 2
    if lst[m] == v:
        return True

    elif lst[m] > v:
        return binary_search(s, m -1, v, lst)

    return binary_search(m+1, e, v, lst)

def main():
    t1 = time.perf_counter_ns() 
    linear_search(55)
    t2 = time.perf_counter_ns() 
    print(f"Time taken to search: {(t2-t1) / 1000} microseconds")

    print(selection_sort(lst))

    t1 =  time.perf_counter_ns() 
    print(binary_search(0, len(lst), 55, lst))
    t2 = time.perf_counter_ns() 
    print(f"Time taken to binary search: {(t2-t1) / 1000} microseconds")


main()