# создание нового словаря
# country_1 = {'name': 'Thailand', 'sea': True}
# country_2 = {'name': 'Hungary', 'sea': False}

# Подход через словари. Тут достаточно просто пройти по ключу, не надо бегать по всему словарю
countries = {
    'Thailand': {'sea': True, 
                'schengen': False,
                'average_temperature': 30,
                'money_amount_per_day': 10, 
                'currency_rate': 1.8},
    'Hungary':  {'sea': False, 
                 'schengen': True,
                 'average_temperature': 10,
                 'money_amount_per_day': 20,
                 'currency_rate': 0.3},
     'Germany': {'sea': True, 
                'schengen': True, 
                'average_temperature': 5,
                'money_amount_per_day': 2, 
                'currency_rate': 80},   
        'Japan':{'sea': True, 
                'schengen': False,
                'average_temperature': 15,
                'money_amount_per_day': 50,
                'currency_rate': 0.61},
        'Mordor':{'sea': False, 
                'schengen': True,
                'average_temperature': 40,
                'money_amount_per_day': 6,
                'currency_rate': 20},
        'Russia':{'sea': False, 
                'schengen': False,
                'average_temperature': 5,
                'money_amount_per_day': 15,
                'currency_rate': 1}}
                
                 
 # Подход через списки []. Нужно проходиться по всему списку чтобы найти страну                
#countries = [
 #   {'name': 'Thailand', 'sea': True, 'schengen': False, 'average_temperature': 30, 'currency_rate': 1.8},
 #   {'name': 'Hungary', 'sea': False, 'schengen': True, 'average_temperature': 10, 'currency_rate': 0.3},
  #  {'name': 'Germany', 'sea': True, 'schengen': True, 'average_temperature': 5, 'currency_rate': 1.5},
  #  {'name': 'Japan', 'sea': True, 'schengen': False, 'average_temperature': 15, 'currency_rate': 1.1}
  #  ]
# название стран теперь отнесены к типу данных строки

# Как заполнять словать
# d = dict()
# d['name'] = 'Thailand'

warm_countries = set()
sea_countries = set()
schengen_countries = set()
money_enough_month = set()


# Множества - удобная структура для операций пересечения и объединения, поддерживает уникальность элементов
# Преимущество списков - порядок, к ним можно обратиться через []. Во множествах порядка нет
# для добавл во множества используется add


money_amount = 10000
for country_name, properties in countries.items():
    currency_amount = money_amount / properties['currency_rate']
    print('У нас будет %.f денег в местной валюте' %  currency_amount)
    
    money_in_month = properties['money_amount_per_day'] *  properties['currency_rate'] * 30

    enough_money = currency_amount - money_in_month
    print('Остается денег на проживание: %.f' % enough_money)
    if enough_money > 0:
        money_enough_month.add(country_name)
        print('Хватит денег, чтобы прожить месяц')
    else:
        print('Денег на проживание не хватит')

for country_name, properties in countries.items():
    if properties['schengen']:
        schengen_countries.add(country_name)
    if properties['sea']:
        sea_countries.add(country_name)
    if properties['average_temperature'] > 20:
        warm_countries.add(country_name)

# print (schengen_countries)
# print (sea_countries)
# print('Страны в Шенгене и с морем:', schengen_countries & sea_countries)
# используем & чтобы найти пересеч множеств
# что то изменилось

sea_schengen_countries = (warm_countries & sea_countries and schengen_countries) & money_enough_month

#for country_name in sea_schengen_countries:
#    for country in countries:
#        if country['name'] == country_name:
#            print(country)
#            break

for country_name in sea_schengen_countries:
    print(country_name, countries[country_name])
    
list(countries.items())
type(countries)