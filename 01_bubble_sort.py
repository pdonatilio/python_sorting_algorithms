# Bubble Sort in Python

# normal bublle sort


def bubble_sort(v):

    len_v = len(v)
    i = len_v - 1

    while i >= 1:
        for j in range(i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]

        i -= 1


def bubble_sort_optimized(v):

    len_v = len(v)   

    for i in range(len_v - 1, 0, -1):
    
        swapped = False

        for j in range(i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                swapped = True

        if not swapped:
            break
    
# normal bublle sort running
v = [10, 40, 5, 15, 30, 70, 20]
bubble_sort(v)
print(v)

# optimized bubble sort running
v = [10, 40, 5, 15, 30, 70, 20]
bubble_sort_optimized(v)
print(v)
