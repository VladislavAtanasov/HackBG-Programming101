def fibonacci(n):
  result = []
  a=1
  b=1
  while len(result)!=n:
 	 result.append(a)
 	 next_fib=a+b
 	 a=b
 	 b=next_fib
  return result
