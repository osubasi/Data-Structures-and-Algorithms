# Omer Subasi

def selfDividingNumbers(left, right):
    def isselfdividing(num):
        tmp = num
        while tmp:
            digit = tmp % 10
            if digit == 0 or num % digit != 0:
                return False
            tmp = tmp // 10
        return True

    res = []    
    for num in range(left, right+1, 1):
        if isselfdividing(num):
            res.append(num)
    return res
