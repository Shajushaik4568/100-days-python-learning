import time
timestamp = time.strftime('%H:%M:%S')
print("The Time Is: ", timestamp)
b = int(timestamp[0:2])
# b=21
print("Hours:",b)

if(b > 0 and b < 12):
  print("Good Morning")

elif(b >11 and b < 17 ):
  print("Good Afternoon")
  
elif(b > 14 and b < 19):
  print("Good Evening")
  
else:
  print("Good Night")
