# Omer Subasi 

def fib(n):
        F = [0] * (n+1)
        if n > 0:
            F[1] = 1
            i = 2
            while i < n+1:
                F[i] = F[i - 1] + F[i - 2]
                i += 1
            
            return F[n]
        else:
            return 0
