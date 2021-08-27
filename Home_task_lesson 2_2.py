list_with_my_information = list(input('Введите Ваши числа (числа необходимо указывать без пробелов): '))
for i in range(1, len(list_with_my_information), 2):
    list_with_my_information[i-1], list_with_my_information[i] = list_with_my_information[i], list_with_my_information[i-1]
print(list_with_my_information)
