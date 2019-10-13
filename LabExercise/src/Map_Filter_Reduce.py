'''Map'''
#map(function_to_apply, list_of_inputs)
from itertools import product

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
    
#print(squared)

squared = list(map(lambda x: x**2, items))

#print(squared)

'''Filter'''
#As the name suggests, filter creates a list
#of elements for which a function returns true. 
#Here is a short and concise example:

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
#print(less_than_zero)


'''Reduce'''

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
#print(product)

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
#print(product)
