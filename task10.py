dict1 = {number:number*229 for number in range(1,6)}
def sum_of_value(d):
    total = 0
    for k,v in d.items():
        total +=v
    return total
    
print(sum_of_value(dict1))
total2 = sum(dict1.values())
print(total2)

def sum_of_value_version2(d):
    return sum(d.values())
print(sum_of_value_version2(dict1))