time = int(input('введите Ваше целое значение количества секунд : '))
while time < 0:
    print('Требовалось ввести целое число больше 0')
    time = int(input('введите Ваше значение количества секунд : '))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print('В', f'{time}', "секундах", f'{hours:02}', 'часов', f'{minutes:02}', 'минут', f'{seconds:02}', "секунд")
print("Вывод результата в требуемом формате", f'{hours:02}:{minutes:02}:{seconds:02}')