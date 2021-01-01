from collections import Counter 
  
# Initial Dictionary 
my_dict = {'A': 67, 'B': 23, 'C': 45,  
           'D': 56, 'E': 12, 'F': 69} 
  
k = Counter(my_dict) 

# Finding 3 highest values 
high = k.most_common(3)  

for i in high:
    print(f'{i[0]} : {i[1]}')