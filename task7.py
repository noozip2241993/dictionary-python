""" Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys."""
dic1 = {number:number**2 for number in range(1,16)}
print(dic1)

def value_double_keys(n):
    d= dict()
    for k in range(1,n+1):
        d[k]=k*k
    return d
print(value_double_keys(15))