def fib_number(n):
    result = ""
    a=1
    b=1
    while n!=0:
        result+=str(a)
        next_fib=a+b
        a=b
        b=next_fib
        n-=1
    return result
print(fib_number(3))
print(fib_number(10))