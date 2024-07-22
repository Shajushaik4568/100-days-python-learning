letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")


price = 49.6399999
print(f"Price of Apples is {price:.4f} dollars")


print(f"{2 * 30}")
print(type(f"{2 * 30}"))  ##O/P as String