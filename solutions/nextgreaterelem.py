# Omer Subasi

def nextGreaterElement(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    ans = [-1 for _ in range(n)]
    mymap = {}
    for i, x in enumerate(nums2):
        mymap[x] = i

    for i, x in enumerate(nums1):
        idx = mymap[x]
        for j in range(idx+1, m):
            if(nums2[j] > x):
                ans[i] = nums2[j]
                break

    return ans
