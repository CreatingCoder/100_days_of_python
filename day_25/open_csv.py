import csv

with open('weather_data.csv') as my_file:
    data = csv.reader(my_file)
    temps = []

    for row in data:
        if row[1] != 'temp':
            temps.append(int(row[1]))
    
print(temps)
