import operator
"""Write a Python program to sort (ascending and descending) a dictionary by value.

"""
numbers = {1:2,3:4,5:6,7:8,2:4}
print('Original dictionary : ',numbers)
sorted_numbers = sorted(numbers.items(),key=operator.itemgetter(1))
print(sorted_numbers)