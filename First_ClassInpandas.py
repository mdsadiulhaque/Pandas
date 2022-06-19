import pandas as pd
data = pd.DataFrame({'Country': ['Russia','Colombia','Chile','Equador','Nigeria'],
'Rank':[121,40,100,130,11]})
print(data)#The call 2d matrix
print('*****************')
print(data.describe())
print('*****************')
print(data.info())
#####
data1 = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
a=data1.sort_values(by=['ounces'],ascending = True, inplace =False)
print(data1.sort_values(by=['group','ounces'],ascending=[True,False],inplace=False))

data2 = pd.DataFrame({'k1':['one']*3 + ['two']*4, 'k2':[3,2,1,3,3,4,4]})
print(data2.sort_values(by='k2'))
print(data2.drop_duplicates())
print(data2.drop_duplicates(subset='k1'))

data3 = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honeyham','nova lox'],
                      'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}
def meat_2_animal(series):
    if series['food'] == 'bacon':
     return 'pig'
    elif series['food'] == 'pulled pork':
        return 'pig'
    elif series['food'] == 'pastrami':
        return 'cow'
    elif series['food'] == 'corned beef':
        return 'cow'
    elif series['food'] == 'honey ham':
        return 'pig'
    else:
        return 'salmon'
data3['animal'] = data3['food'].map(str.lower).map(meat_to_animal)
print(data3)