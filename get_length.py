#find count of digits in an integer without using for, len, while
def get_length(num):
    count=0
    while num>0:
        count=count+1
        num=num//10
    return count

print(get_length(15))