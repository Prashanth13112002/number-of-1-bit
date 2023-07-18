def number_of_one(num):
    a=0
    while num:
        a+=num&1
        num>>=11
    return a
num=int(input())
print(number_of_one(num))

