# Selection Sort in Python
# Complexity: 
#   All cases: O(n²)


def selection_sort(v):

    len_v = len(v)

    for i in range(len_v - 1):

        smallest = i  # The position of smallest iten on array

        for j in range(i + 1, len_v):
            if v[j] < v[smallest]:
                smallest = j

        v[i], v[smallest] = v[smallest], v[i]


v = [1, 3, 2, 4]
selection_sort(v)
print(v)

v = [50,40,58,59,74,20,12,26]
selection_sort(v)
print(v)