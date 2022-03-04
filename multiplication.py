def puissance(n):
    
    x = 0
    y = 0
    
    while (y <= n):

        y = 2**x
        x += 1

    return y//2

def multi(num1,num2):

    if num1 == 1 and num2 == 1:
        return 1

    elif (num1 != num2 and (num1 == 1 or num2 == 1)):
        return max(num1,num2)

    elif num1 == 0 or num2 == 0:
        return 0

    else:

        a = min(num1,num2)
        b = max(num1,num2)
        c = 0
        i = 0
        multi = 0

        d = {}

        while True:

            k = puissance(a)
            i = k
            a = a - i

            while i != 0:
                c += b 
                i -= 1
            d[k] = c
            c = 0
            
            if a == 0:
                
                break
        print(d)
        for key in d.keys():
            multi += d[key]

        return multi
