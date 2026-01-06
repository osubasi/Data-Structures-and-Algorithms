# Omer Subasi

def plusOne(digits):
    c = 0
    for i in range(len(digits) - 1, -1, -1):
        if i == len(digits) - 1:
            tmp = digits[i] + 1
            if tmp >= 10:
                digits[i] = tmp - 10
                c = 1
            else:
                digits[i] = tmp
                c = 0
        else:
            tmp = digits[i] + c
            if tmp >= 10:
                digits[i] = tmp - 10
                c = 1
            else:
                digits[i] = tmp
                c = 0
    
    if c == 1:
        digits = [1] + digits

    return digits
