def is_prime(n):
    if n==1 or n<0:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n
def divide_count(n, k):
    times = 0
    while n != 1 and n % k == 0:
        times += 1
        n = n // k
    return times
def prime_factorization(n):
    result = []
    current_prime = 2
    while n != 1:
        times = divide_count(n, current_prime)
        if times != 0:
            result.append((current_prime, times))
            n = n // current_prime ** times
        current_prime = next_prime(current_prime)
    return result

#def is_prime(n):
#    if n==1 or n<0:
#        return False
#    else:
#        for i in range(2,n):
#            if n%i==0:
#                return False
#        return True
#def divisors(n):
#    lis=[]
#    for i in range(2,n+1):
#        if n%i==0 and is_prime(i):
#            lis.append(i)
#    return lis
#def times(n):
#    count = 0
#    #for i in range(2,n+1):
#    #    if n%i == 0 and is_prime(i):
#    #        count+=1
#    #return count
#    lis1 = []
#    for i in divisors(n):
#
#    return lis1
#def prime_factorization(n):
#    arr = []
#    result = divisors(n)
#    new = times(n)
#    if len(result) == 1:
#        fin = [(y, int(z)) for y in result for z in str(new) if n == y**int(z)]
#        return fin
#    else:
#        fin = [(y, int(z)) for y in result for u in result  for z in str(new) if n == (y**int(z))*(u**int(z))]
#        return fin


print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))
print(prime_factorization(1000))
