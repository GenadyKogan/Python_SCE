            #MAP
#map(function_to_apply, list_of_inputs)
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
    
items = [1, 2, 3, 4, 5]
y=2
squared = list(map(lambda x: x**y, items))
print(squared) 
            #FILTER
number_list = range(-5, 6)
less_than_zero = list(filter(lambda x: x <0, number_list))


            #Reduce
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
    
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])  
print(product)  