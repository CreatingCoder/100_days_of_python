import pandas

data = pandas.read_csv('weather_data.csv')

temp_list = data.temp.tolist()


# high_temp = 0
# for temp in temp_list:
#     if temp > high_temp:
#         high_temp = temp
# print(high_temp)

# high_temp = data.temp.max()

# print(data[data.temp == data.temp.max()])


# sunday = data[data.day =='Sunday']
# sunday.temp = sunday.temp * 1.8 + 32
# print(sunday)


data_dic = {
    'students': ['John', 'Alex', 'Fred'],
    'scores' : [78,56,66]
}

new_table = pandas.DataFrame(data_dic)
print(new_table)

new_table.to_csv('new_table.csv')
 
