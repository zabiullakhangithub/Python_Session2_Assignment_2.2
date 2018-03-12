# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:49:48 2018

@author: zabiulla.khan


Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

"""

#print({x:x**2 for x in range(10)})
from functools import reduce

# Loop through all chars in the string and display the output as list
print([chars for chars in 'ACADGILD'])

# Define list comprehension as per line#2 as display the output
print(reduce(lambda x1,x2:x1+x2, [[n,n*2,n*3,n*4] for n in ['x','y','z']]))
list1 = ['x','y','z']

# Define list comprehension as per line#3 as display the output
print(reduce(lambda x1,x2:x1+x2, [[n for n in list1],[n*2 for n in list1],[n*3 for n in list1],[n*4 for n in list1]]))

# Define list comprehension as per line#4 as display the output
list2=[1,2,3]
print([[n+1] for n in list2],[[n+2] for n in list2],[[n+3] for n in list2])

# Define list comprehension as per line#5 as display the output
list3=[1,2,3,4]
print([n+1 for n in list3],[n+2 for n in list3],[n+3 for n in list3],[n+4 for n in list3])

# Define list comprehension as per line#6 as display the output
print([(j, i) for i in [1,2,3] for j in [1,2,3]])