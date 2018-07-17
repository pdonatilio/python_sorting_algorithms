# Tim Sort using Objects in Python
# Example to Ordenate a object by an attribute
# Complexity:
#   Worst Case: O(n Log(n))*
#   Best Case: O(log2(n!))*
#   *based on wikipedia

import operator
from tim_sort_fuctions import *


class People():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


people_list = []

# Creating an array with aleatory data
for i in range(10):
    people_list.append(People(generate_string(10), generate_number(70)))

print('Not Ordered list:')
# Showing the list not ordered
for people in people_list:
    print('Name: %s, Age: %d' % (people.get_name(), people.get_age()))

# Ordernating the list by an object's attribute
people_list.sort(key=operator.attrgetter('age'))

print()
print('Ordered list:')

# Showing the list ordered by attribute
for people in people_list:
    print('Name: %s, Age: %d' % (people.get_name(), people.get_age()))
