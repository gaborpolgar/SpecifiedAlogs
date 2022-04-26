import timeit
import random as rd

def linear_search(v, T):
    for i in range(0, len(v)):
        if v[i] == T:
            return i
    return -1

def strazsasKereses(v, T):
    i = 0

    while v[i] != T:
        i += 1

    if i < len(v)-1:

        return i  # vagy True

    else:

        return -1  # False

def feltolt(v, n, n_max):
    for i in range(0, n):
        v.append(rd.randint(1, n_max))

    return v

arr = []
feltolt(arr, 10_000_000, 1_000_000)
arr[len(arr) - 1] = 100_000

start = timeit.default_timer()

linear_search(arr, 10)

stop = timeit.default_timer()

print(stop - start)

start = timeit.default_timer()

strazsasKereses(arr, 10)

stop = timeit.default_timer()

print(stop - start)
