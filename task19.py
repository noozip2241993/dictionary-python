"""Write a Python program to combine two dictionary adding values for common keys. """
from collections import Counter
def combining_two_values_dic(d1,d2):
    return Counter(d1) + Counter(d2)
dic1 = {'a': 100, 'b': 200, 'c':300}
dic2 = {'a': 300, 'b': 200, 'd':400}
print(combining_two_values_dic(dic1,dic2))