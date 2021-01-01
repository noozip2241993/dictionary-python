""" Write a Python program to multiply all the items in a dictionary. """
def multiply_all(d):
    total = 1
    for k,v in d.items():
        total *=v
    return total
dic1 = {number:(number+2)*5 for number in range(1,6)}
print(dic1)
print(multiply_all(dic1))