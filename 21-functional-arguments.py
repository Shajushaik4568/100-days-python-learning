def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")                                    ## Default argurments
name("Amy",mname= "Shaik", lname= "Shaaj")     ## Keyword Arguments


numbers=[10,6,3,29,12,1,90,35]
def avg(*numbers):
  sum=0
  for i in numbers:
    sum=sum+i
  average=((sum)/len(numbers))
  print("SUM is :", sum)
  # print(average)
  return average

print("AVERAGE is : ", avg(*numbers))        ## Variable length Arguments

                                             ## RETURN STATEMENTS
def dude(fname, mname, lname):
  return "Hello, " + fname+" " + mname+" " + lname

print(dude("Shyam","Singha","Roy"))
