a = "!!Shaaj is An aspirant of Python ... !!!"
print(a)
print ( len (a))
print(a.upper())
print(a.lower())
print(a.strip("!"))
print(a.rstrip("!"))
print(a.replace("Shaaj","Praveen"))
print(a.find("an"))
print(a.find("z"))
# print(a.index("z")) ### will fail the program if string is not found
b=" "
print(a.split(b))
c="   to Kill A Mockingbird"
print(c.capitalize())
print(c.title())
print(c.count("l"))
print("ends with !!! ?", a.endswith("!!!"))
d="Subtle art of not giving f0ck"
print(d.center(50), "Done")
d="yesimalphanumeric123\n"
print("\nString=",d)
print(d.isalpha())
print(d.isalnum())
print("Is title?", d.istitle())
print("Uppercheck:", d.isupper())
print("Lowercase_Check:", d.islower())
print("Is printable ?",d.isprintable())
print("Is starts with \"yes\":", d.startswith("yes"))
print("Any blank spaces? :", d.isspace())
print("Lets Swap ::", d.swapcase())
