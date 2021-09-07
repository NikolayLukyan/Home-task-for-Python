from random import randint

with open('my_nw_file.txt', 'w', encoding='utf-8') as my_best:
    list = [randint(1, 250) for _ in range(100)]
    my_best.write(''.join(map(str, list)))

print(f'The sum of all elements in list is {sum(list)}')
