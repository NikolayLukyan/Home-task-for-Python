user_number = int(input("Введите свое целое число больше 0: "))
biggest_dig = user_number % 10  # Присваиваем самое большее значение последней цифре введенного значения
other_dig = user_number  # Переменная для временного хранения значений введенного числа для цикла
while other_dig > 0:
    dig = other_dig % 10
    if dig > biggest_dig:
        biggest_dig = dig
        if biggest_dig == 9:
            break
    other_dig = other_dig // 10
print('максимальная цифра в числе', user_number, "является", f'{biggest_dig}')
