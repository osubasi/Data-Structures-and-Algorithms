# Omer Subasi

def maxArea(height):
    n = len(height)
    if (n == 2):
        return min(height)

    if (n == 3):
        return max(min(height[0], height[1]), min(height[1], height[2]), min(height[0], height[2]) * 2)

    l = 0
    r = n - 1
    fmax = 0
    curr = 0
    while l < r:
        curr = min(height[l], height[r]) * (r - l)
        fmax = max(fmax, curr) 
        if height[l] < height[r] or height[l] < height[l+1]:
            l += 1
        elif height[r] < height[r-1] or height[l] > height[r]:
            r -= 1
        else:
            l += 1
            r -= 1

    if (height[0] == 0 and height[1] == 1):
        return fmax * 2

    return fmax
