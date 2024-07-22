l=[12, 56,"Shaaj", True, 1.6934534, 34,12, 2432, 224,87, 12]
num=[12, 234, 34, 124, 2553, 3, 20]
# print(l)
# print(type(l))
# for i in range(len(l)):
#   print(l[i])
print(l)
l.append(145)
print(l)
###
num.sort()
print("SORTED ORDER:",num)
num.sort(reverse=True)
print("REVERSE ORDER: ", num)
###

print(l.index(34))
print("Countof '12'  :",l.count(12))

if (34 in l):
  print("YES")
# m=l.copy()
# print(m)

# l.insert(1, 889)  # Inserts 889 at index 1
# print(l)
# l.extend(num)
# print(l)
# k=l+num
# print(k)

lst=[i*i for i in range (10)]
print(lst)
lst=[i*i for i in range (10) if i%2==0]
print(lst)
lst=[i*i for i in range (10) if i%2!=0]
print(lst)