#Find the sum of digits in an integer
def get_length(num):
    count=0
    x1=num%10
    num//=10
    x2=num%10
    num//=10
    x3=num%10
    num//=10
    x4=num%10
    num//=10
    x5=num%10
    num//=10

    count = x1+x2+x3+x4+x5
    return count

print(get_length(555))