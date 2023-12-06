#!/usr/bin/env python3
"""
Sort algorithms
input: nums - a list of integers
output: a sorted list of nums in ascending order
"""
# Bubble Sort
def bubble1(nums: list) -> list:
    n = len(nums)
    for i in range(n):
        for j in range(n-1, i, -1):
            if nums[j-1] > nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums


# Selection Sort
def selection1(nums: list) -> list:
    n = len(nums)
    for i in range(n-1):
        smallest = i
        for j in range(i+1, n):
            smallest = j if nums[j] < nums[smallest] else smallest
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums


# Insertion Sort
def insertion1(nums: list) -> list:
    '''
    InsertionSort(A[n])
        InsertionSort(A[n-1])
        Insert(A[n], A[n-1])
    '''
    n = len(nums)
    for i in range(1, n):
        insert = nums[i]
        j = i-1
        while (j >= 0 and insert < nums[j]):
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = insert
    return nums


# Merge Sort
def mergesort1(nums: list) -> list:
    '''
    Mergesort
    1) divide: split the list
    2) conquer: combine two sorted list
    3) base case: if length <= 1: already sorted
    '''
    n = len(nums)
    if n <= 1:
        return nums
    return list(_mergesort2(mergesort1(nums[:n//2]), mergesort1(nums[n//2:])))

# _mergesort v1
def _mergesort1(a, b):
    i, j = 0, 0
    na, nb = len(a), len(b)
    merged = []
    # This looks bad
    while (len(merged) < na + nb):
        if i == na:
            merged.append(b[j])
            j += 1
        elif j == nb:
            merged.append(a[i])
            i += 1
        else:
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
    return merged

# _mergesort v2: better
def _mergesort2(a, b):
    la, lb = len(a), len(b)
    i, j = 0, 0
    while i < la or j < lb:
        if i == la or (j != lb and a[i] > b[j]):    # 
            yield b[j]
            j += 1
        else:
            yield a[i]
            i += 1


# Quicksort
def quicksort1(nums: list) -> list:
    '''
    1) divide:
        - set a pivot
        - divide the list into left (smaller or equal to the pivot) and
        right (larger than the pivot)
    2) conquer: concatenate
    '''
    n = len(nums)
    if n <= 1:
        return nums
    
    pivot = nums[0]
    left = [x for x in nums[1:] if x <= pivot]
    right = [x for x in nums[1:] if x > pivot]
    return quicksort1(left) + [pivot] + quicksort1(right)

# Heapsort
def _heapsort(nums: list):
    import heapq
    heapq.heapify(nums)
    for _ in range(len(nums)):
        yield heapq.heappop(nums)

heapsort1 = lambda nums: list(_heapsort(nums))

# Radix Sort

# Counting Sort


if __name__ == "__main__":
    nums = [*range(10, -11, -1)]
    nums = [68, 51, -16, -49, 2, -20, 56, -40, -5, 16, 81, 0, -44, 51, 23, -50, 81, 96, 62, 80, -38, 45, 79, 36, -6, -80, -14, 22, 82, 93, -5, 73, -48, 61, 9, -98, 43, -21, 64, 33, -100, -2, 73, -52, -35, 74, -62, 13, -53, 93, 60, -11, -84, -36, 1, 86, -79, 10, 41, 9, 62, 8, 92, 20, 17, -12, 19, -24, 15, -42, -63, -63, 22, 31, -5, -83, 51, 75, 84, 68, 79, 84, 8, -22, 41, -45, 62, 69, 79, 17, 89, 15, -10, 32, 99, 83, 58, -84, 22, -3]
    print(nums)
    print(mergesort1(nums))
    print(nums)
