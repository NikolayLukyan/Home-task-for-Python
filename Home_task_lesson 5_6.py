dic = {}
with open('text_6.txt', encoding='utf-8') as my_best:
    for line in my_best:
        name, status = line.split(':')
        sum_name = sum(map(int,''.join([i for i in status if i == ' ' or '9' >= i >= '0' ]).split()))
        dic[name] = sum_name
print(f'{dic}')