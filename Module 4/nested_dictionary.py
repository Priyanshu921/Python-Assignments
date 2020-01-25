people={1:{'name':'Lucifer','age':100,'sex':'Female'},2:{'name':'Lalchand','age':12,'sex':'male'}}
for i in range(0,2):
    print(people[i+1]['name'])
print('After Adding new elements')
people[3]={}
people[3]['name']='Gracy'
people[3]['Age']=20
people[3]['sex']='Female'
print(people[3])
people[4]={'name':'Lucy','age':1000,'sex':'Female'}
print(people[4])
del(people[4]['age'])
print(people[4])
for p_id,p_info in people.items():
    print("\nPerson Id:",p_id)
    for key in p_info:
        print(key+":",p_info[key])
