# Omer Subasi

def complexNumberMultiply(num1, num2):
        def strtocomplex(s):
            for i, c in enumerate(s):
                if c == "+":
                    a = int(s[:i])
                    b = int(s[i+1:-1])
                    return a, b
            return 0, 0
        
        a, b = strtocomplex(num1)
        c, d = strtocomplex(num2)
        #print(a, b, c, d)
        r = a*c - b*d
        i = b*c + a*d

        return str(r) + "+" + str(i) + "i"
