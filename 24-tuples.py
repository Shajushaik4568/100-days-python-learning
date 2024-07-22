tup = (1, 2, 76, 342, 32, "green", True)
print(type(tup),tup)
for i in range(len(tup)):
  print(tup[i])

if 76 in tup:
  print("YES 76 is in the tuple")
else:
  print("NO 76 is NOT in the tuple")

tup2=tup[1:5]   ##SlICING
print(tup2)

## Modifications to tuple
# print(type(tup))
# print(tup)
# l=list(tup)
# print(type(l))
# l.append( 44)
# tup=tuple(l)
# print(tup)
# print(type(tup))



# # tup[0] = 90
# print(type(tup), tup)
# print(tup[2])
#print(tup[34]) will throw error as 34 index is not there !!! IndexError: tuple index out of range