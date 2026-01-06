# Omer Subasi

import heapq    
def findKthLargest(nums, k):
    min_heap = []
    for x in nums:
        heapq.heappush(min_heap, x)
        if (len(min_heap) > k):
            heapq.heappop(min_heap)
    
    return min_heap[0]
