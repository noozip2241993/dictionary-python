"""Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)"""
def generating_dictionary_contains_number(n):
    d = dict()
    for k in range(1,n+1):
        d[k]=k*k
    return d
print(generating_dictionary_contains_number(20))
