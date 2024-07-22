# def gmean(a,b):
#   gm=(a*b)/(a+b)
#   return gm

# print("enter 2 Values")
# a=int(input("Values of a: "))
# b=int(input("Values of b: "))
# i=gmean(a,b)
# print(f"G-Mean of {a} & {b}: ",i)

def isgreater(a,b):
  if (a>b):
    print(f"RESULT: {a} is GreaterThan {b}")
  elif(b>a):
    print(f"RESULT: {a} is NOT GreaterThan {b}")
  else:
    print(f"RESULT: {a} is EQUAL to {b}")

isgreater(10,7)
