## allows you to use the functions and variables defined in the module in your current script, 
## as well as any additional modules that the imported module may depend on.

import math

result = math.sqrt(9)
print(result)  # Output: 3.0

from math import sqrt, pi
# from math import pi, sqrt as s

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793

#####

from math import *  ## But it is NOT recommended as it could cause issueswith variables
## Alternatively --> import math    ### importing whole module is better


### "as" KEY WORD
import math as m

result = m.sqrt(9)
print(result)  # Output: 3.0

print(m.pi)  # Output: 3.141592653589793

#__________________________________________________________________________________________________________________
## Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. 

import math
print(dir(math))