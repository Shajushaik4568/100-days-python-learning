# x=int(input("enter a value to find its factorial:"))
    
# def f(n):
#   if(n==0 or n==1):
#     return 1
#   else:
#     return f(n-1)*n

# print(f(x))

def fib(n):
  sum1=0
  sum2=1
  result=0
  for i in range(n):
    result=int(sum1)+int(sum2)
    sum1=sum2
    sum2=result
    
  return result

print(fib(10))
    