month = int(input('Введите число месяца (числа могут быть только от 1 до 12): '))
list_month = ['январь',	'февраль',	'март', 'апрель', 'май', 'июнь', 'июль', 'август',
              'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
dict_season = {1: 'зима' ,	2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето',9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
if month in dict_season:
    print(f'{month}-й месяц это {list_month[month-1].upper()}. Соответсвует времени года - {dict_season[month].upper()}.')
else:
    print ("Вы ввели некорректное значение для месяца года")