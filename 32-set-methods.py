# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")

##union() and update():   The union() and update() methods prints all items that are present in the two sets.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.union(cities2)
print(cities3)

cities.update(cities2)
print(cities)

#Intersection
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities4 = cities.intersection(cities2)
print(cities4)

cities.intersection_update(cities2)
print(cities)

## Symmetric_difference and symmetric_difference_update():
###   The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities5 = cities.symmetric_difference(cities2)
print(cities5)

## difference & difference_update
####   The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities6 = cities.difference(cities2)
print(cities6)