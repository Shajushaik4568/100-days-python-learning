# i=int(input("enter a number"))
# if (i>5):
#   print("Enter a values only between 0 & 5")
# else:
#   while(i <= 5 and i>=0):
#     print("Value of i is : ",i)
#     i=i-1
#   else:
#     print("END OF THE LOOP")

#### PYTHON DOESNT HAVE IN BUILT "do-while" loop. below is the simulation of "do-while Loops"
## do while
# i=1
# while True:
#   print(f"This is {i} Iteration")
#   i=i+1
#   if (i >=5):
#     break

i=int(input("Enter any number"))
count=0
print("printing Next 5 numbers")
while True:
  print(f"+{count} of your entry:",i+count)
  count=count+1
  if (count==5):
    break