# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")

try:      ## try is added whenever there is scope of program failure
  num = int(input("Enter an integer: "))
  a = [6, 3]
#   b=(num/0)
  print(a[num])
except ValueError:
  print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")

except FileNotFoundError:
  print("FileNotFoundError: FILE NOT FOUND")

except ZeroDivisionError:
  print("Cannot divide with zero")

finally:            ###  When we handle exception using the try and except block,
                    ###  we can include a finally block at the end
                    ###  The finally block is always executed
  print("I am always executed")
  print("The finally block is always executed")

    