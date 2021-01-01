from itertools import product




#x={'1':['a','b','f'], '2':['c','d','e']}
#list1 = x.get('1')
#list2 = x.get('2')
#for i in range(3):
    #for j in range(3):          
     # print(list1[i]+list2[j])
#print(list1)


#d ={'1':['a','b'], '2':['c','d']}
#for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    #print(''.join(combo))

x={'1':['a','b','f'], '2':['c','d','g'],'3':['t','y','v']}
list1 = x.get('1')
list2 = x.get('2')
list3 = x.get('3')
d = (list(product(list1,list2,list3)))
print(d)

for i in d:
    k = '{}{}{}'.format(i[0],i[1],i[2])
    print(k)