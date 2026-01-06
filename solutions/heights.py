# Omer Subasi

import random

def heightChecker(self, heights: List[int]) -> int:
    expected = [x for x in heights]
    def partition(arr, l, r):
        p = r
        l1 = l
        for i in range(l, r, 1):
            if(arr[i] < arr[p]):
                tmp = arr[i]
                arr[i] = arr[l1]
                arr[l1] = tmp
                l1 += 1
        tmp = arr[p]
        arr[p] = arr[l1]
        arr[l1] = tmp
        return l1

    def qsort(arr, l, r):
        if l < r:
            p = partition(arr, l, r)
            qsort(arr, l, p - 1)
            qsort(arr, p + 1, r)

    qsort(expected, 0, len(expected)-1)
    
    cnt = 0
    for i in range(len(heights)):
        if expected[i] != heights[i]:
            cnt += 1
    return cnt
