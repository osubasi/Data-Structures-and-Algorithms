# Omer Subasi

def fizzBuzz(n):
    res = [None] * (n + 1)
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res[i] = "FizzBuzz"
        elif i % 3 == 0:
            res[i] = "Fizz"
        elif i % 5 == 0:
            res[i] = "Buzz"
        else:
            res[i] = str(i)
    
    return res[1:]
