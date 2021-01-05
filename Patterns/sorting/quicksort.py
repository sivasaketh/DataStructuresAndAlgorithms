import random

def quick_sort(A):
    quick_sort_helper(A, 0, len(A)-1)
    print(A)


def quick_sort_helper(A, l, h):
    if l>=h:
        return
    random_index = random.randint(l,h)
    A[random_index], A[l] = A[l], A[random_index]
    pivot = A[l]
    smaller = l
    bigger = l

    for bigger in range(l, h+1):
        if (A[bigger]<pivot):
            smaller+=1
            A[smaller], A[bigger] = A[bigger], A[smaller]
    A[l], A[smaller] = A[smaller], A[l]
    quick_sort_helper(A, l, smaller-1)
    quick_sort_helper(A, smaller+1, h)


quick_sort([1,3,4,5,6,2])

