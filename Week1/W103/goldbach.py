def is_prime(n):
    if n==1 or n<0:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
def prime_divisor(n):
    new = []
    for x in range(2,n+1):
        if is_prime(x):
            new.append(x)
    return new

def goldbach(n):
    new = [(x,y) for x in range(2,n) for y in range(2,n) if x in prime_divisor(n) and y in prime_divisor(n) and x+y==n and x<=y]
    return new
print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))
