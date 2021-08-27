my_information = input('Введите строку (слова надо разделять пробелами) : ').split()
for i, word in enumerate(my_information, 1):
    print(f'{i}. {word[:10]}.')
