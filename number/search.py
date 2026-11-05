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

def main():
    start = time.perf_counter_ns()
    linear_search(55)
    end = time.perf_counter_ns()
    print(f"Time taken to search: {(end-start) / 1000} microseconds")

    print(selection_sort(lst))

main()