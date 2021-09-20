def func_to_sum():
    i = 0
    while True:
        my_list = input('Enter numbers which you want to sum, input "D" for exit programme ').split()
        for arg in my_list:
            if arg.upper() == "D":
                return i
            else:
                try:
                    i = i + int(arg)
                except ValueError:
                    print('If you want to exit programme than input "D"')
        print(f'The result of summarize your numbers is {i}')


print(func_to_sum())
