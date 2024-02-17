def func(num):
    if num==0:
        return 1
    else:
        return num*func(num-1)

n=int(input())

print(func(n))