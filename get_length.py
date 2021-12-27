#find count of digits in an integer without using for, len, while
def get_length(num):
    x1 = pow(0, num)
    num//=10

    x2 = pow(0, num)
    num//=10

    x3 = pow(0, num)
    num//=10

    x4 = pow(0, num)
    num//=10

    x5 = pow(0, num)
    
    return 5 - (x1 + x2 + x3 + x4 + x5)

print(get_length(15))