time =  int(input("Enter the current time(24hrs):  "))
print("Good Morning!!!") if time <= 11 else print("Good Afternoon") if ( time > 11 and time < 16 ) else  print("Good Evevning")
#'___________________________________' '_________________________________________________________' '___________________________'
c = 9 if time < 12 else 0
print(c)