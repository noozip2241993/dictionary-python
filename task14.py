import operator
def sorting_dict_by_key(d):
    return sorted(d.items(), key=operator.itemgetter(0),reverse=False)
dic1 = {numbers:numbers*6 for numbers in range(1,6)}

dict2 ={'Khang': 'Jack', 'Trang': 'Kristy', 'Me': 'Tho', 'Ba': 'Ninh'}
print(sorting_dict_by_key(dict2))