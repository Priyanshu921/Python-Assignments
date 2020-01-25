fruits={1:{'name':'Apple','scientific name':'Malus domestica','producers':['United States','Turkey'],'neutrition values':{'carbohydrates':'13.81g','fat':'0.17g','protein':'0.26g'}},
        2:{'name':'Mango','scientific name':'Mangifera indica','producers':['Índia','China','Thailand'],'neutrition values':{'carbohydrates':'15g','fat':'0.4g','protein':'0.8g'}},
        3:{'name':'Guava','scientific name':'Psidium guajava','producers':['Índia','China','Thailand'],'neutrition values':{'carbohydrates':'14g','fat':'1g','protein':'2.6g'}},
        }
pro=[]
for i in range(1,4):
    pro.append(fruits[i]['neutrition values']['protein'])
print(fruits[pro.index(max(pro))+1]['name'])
print(max(pro))
pro=[]
for i in range(1,4):
    if ('China' in fruits[i]['producers']):
        pro.append(fruits[i]['neutrition values']['protein'])
print(fruits[pro.index(max(pro))+1]['name'])
print(max(pro))
