"""Write a Python program to get the maximum and minimum value in a dictionary"""
def maximum_value(d):
    maximum1 = -100000000000
    for i in d.values():
        if i > maximum1:
            maximum1 = i
    return maximum1
dic1 = {numbers:numbers*10 for numbers in range(1,6)}
print(maximum_value(dic1))
print(dic1)
def minimum_value(d):
    minimum1 = 100000000000
    for i in d.values():
        if i < minimum1:
            minimum1 = i
    return minimum1
print(minimum_value(dic1))

print(max(dic1.values()))