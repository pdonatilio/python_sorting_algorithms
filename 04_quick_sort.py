# Quick Sort in Python
# Complexity:
#   Worst Case: O(n²)
#   Best Case: O(n LG(n))


def parted(v, start, end):
    # the pivot is the first element
    pivot = start

    for i in range(start + 1, end + 1):
        if v[i] <= v[start]:
            pivot += 1
            v[i], v[pivot] = v[pivot], v[i]

    v[pivot], v[start] = v[start], v[pivot]

    return pivot


def quick_sort(v, start, end):
    '''
        If the end is bigger than start, so 
        we need to calculate the pivot position.
        To do this we create an function called parted
    '''

    if end > start:
        # separe in two parts
        pivot = parted(v, start, end)

        '''
            when we've the pivot, call the function parted again,
            at the first time we get the elements before the pivot
            and in the second call we get the elements after the pivot
        '''
        quick_sort(v, start, pivot - 1)
        quick_sort(v, pivot + 1, end)


v = [4,2,3,1]
quick_sort(v, 0, len(v) - 1)
print(v)

v = [50, 40, 12, 14, 23, 54, 2, 1, 5, 4]
quick_sort(v, 0, len(v) - 1)
print(v)


#creating a big array
import random
v = []
for i in range(100):
    v.append(random.randint(1,100))

print(v)
quick_sort(v, 0, len(v) - 1)
print(v)