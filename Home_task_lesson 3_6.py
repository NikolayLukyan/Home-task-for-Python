def my_new_func(symbol):
    my_list = 'zxcvbnmasdfghjklqwertyuiop'
    return symbol.title() if not set(symbol).difference(my_list) else False


symbol = input('Enter your words in lower latin with space: ').split()
for i in symbol:
    result = my_new_func(i)
    if result:
        print(my_new_func(i),' ')
