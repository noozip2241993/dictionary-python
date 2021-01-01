"""Write a Python program to remove a key from a dictionary."""
dic1 = {number:number*3 for number in range(1,6)}
def removing_key_dictionary(d):
    if 1 in d:
        del d[1]
    return d
print(removing_key_dictionary(dic1))
