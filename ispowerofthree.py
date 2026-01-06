# Omer Subasi

def isPowerOfThree(n):
        if n <= 0:
            return False
        return not bool(log10(abs(n))/log10(3) - int(log10(abs(n))/log10(3)))
