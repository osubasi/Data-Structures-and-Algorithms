# Omer Subasi

def majorityElement(nums):
    #return Counter(nums).most_common(1)[0][0]
    cand = -1
    cnt = 0
    for x in nums:
        if cnt == 0:
            cand = x
            cnt = 1
        elif x == cand:
            cnt += 1
        else:
            cnt -= 1
    cnt = 0
    for z in nums:
        if z == cand:
            cnt += 1
    if cnt > len(nums) // 2:
        return cand
    else: 
        return -1
