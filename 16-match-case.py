a = int(input("Enter Value of a: "))
match a:
  case 0:
    print("Values of a is ZERO")
  case _ if a!=90:
    print("Values of a is NOT 90")
  case _:
    print("default case")