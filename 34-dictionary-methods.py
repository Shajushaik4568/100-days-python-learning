ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
print(ep1) 

ep1.pop(122)   ###The pop() method removes the key-value pair whose key is passed as a parameter.
print(ep1) 

ep1.popitem()  ##The popitem() method removes the last key-value pair from the dictionary.
print(ep1) 


del ep1[123]    ###(Similar to pop) We can also use the del keyword to remove a dictionary item.
print(ep1) 

ep1.clear()   ## The clear() method removes all the items from the list.
print(ep1)