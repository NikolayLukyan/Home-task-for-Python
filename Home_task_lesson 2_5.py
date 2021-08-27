list_with_my_numbers = [8, 7, 7, 5, 4]
number_for_add = int(input('Введите новый элемент рейтинга (только натуральное число) : '))
i = 0
for n in list_with_my_numbers:
    if number_for_add <= n:
        i = i + 1
    else:
        break
list_with_my_numbers.insert(i, number_for_add)
print(list_with_my_numbers)
