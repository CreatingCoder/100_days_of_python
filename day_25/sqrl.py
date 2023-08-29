import pandas

data = pandas.read_csv('2018_census.csv')
df = pandas.DataFrame(data)

gray = df['Primary Fur Color'].value_counts()['Gray']
black = df['Primary Fur Color'].value_counts()['Black']
cinn = df['Primary Fur Color'].value_counts()['Cinnamon']

sqrl_dict = {
    "Fur Color":['Gray', 'Black', 'Cinnamon'],
    'Count': [gray, black, cinn]
}

df = pandas.DataFrame(sqrl_dict)
df.to_csv('updated_sqrl.csv')



