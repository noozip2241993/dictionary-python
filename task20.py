"""Write a Python program to print all unique values in a dictionary. """
dict1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

def unique_values(dic):
    d =set()
    for i in dic:
        for j in i.values():
            d.add(j)
    return d
    
print(unique_values(dict1))
