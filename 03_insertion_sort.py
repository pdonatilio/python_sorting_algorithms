# Insertion Sort in Python
# Complexity: 
#   worst case: O(n²) 
#   best case: O(n)


def insertion_sort(v):

    len_v = len(v)

    for i in range(1, len_v):
        key = v[i]

        j = i - 1
        while j >= 0 and v[j] > key:
            v[j + 1] = v[j]
            j -= 1

        v[j + 1] = key

v = [4, 3, 2, 1]
insertion_sort(v)
print(v)

v = [50,10,5,60,40,70]
insertion_sort(v)
print(v)
