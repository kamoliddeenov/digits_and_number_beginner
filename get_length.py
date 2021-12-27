#find count of digits in an integer without using for, len, while
def get_length(num):
    x = 0
    x -= pow(0, num)
    num//=10
    x -= pow(0, num)
    num//=10
    x -= pow(0, num)
    num//=10
    x -= pow(0, num)
    num//=10
    x -= pow(0, num)
    
    return x+5

print(get_length(100))