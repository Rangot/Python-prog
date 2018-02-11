#preaty print - красиво печатает словари, списки и пр.
from pprint import pprint

# эта конструкция сама потом закрывает вам файл
temp = []
with open('temperature.py') as t:
    for line in t:
        temp.append(int(line))
        
# print(temp)

avg = sum(temp)/len(temp)
# print(avg)

with open ('Avg_temperature.txt','w') as avg_t:
    avg_t.write('%.2f' % avg)
    
temp_dev = []

for t in temp:
    temp_dev.append(t - avg)
    # print(temp_dev)
    
with open ('temp_dev.txt','w') as t_dev:
    for i in temp_dev:
       t_dev.write('%.2f\n' % i)
    
cities = {}

with open ('Week_temp_city.py') as f_w_t:
    for city in f_w_t:
        # print('city:', city)
        temp = f_w_t.readline()
        # print('temp:', temp)
        cities[city.strip()] = temp.split()
        
for city, temp in cities.items():
    avg = 0
    for t in temp:
        avg += int(t)
    avg = avg/len(temp)
    print(city,avg)
pprint(cities)

# как создать файл если его нет
def read_or_create():
    filename = 'file_not_exists'
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
                with open(filename, 'w') as f:
                    pass

# read_or_create()