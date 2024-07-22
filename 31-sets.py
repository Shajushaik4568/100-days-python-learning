s={12, "recusion", False, 26.999,94,1011}
print(type(s),"\n",s)

for value in s:
  print(value)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")


### Set Methods
s1={12,24,67,24,95,232,129, "Pablo","Emilio"}
s2={"Escobaro","Gaiveria",24,67,245,45,92,33}
print(s1.union(s2))
print(s1.difference(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
# print(s1.difference(s2))

s1.intersection_update(s2)
print(s1)

s3={}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))