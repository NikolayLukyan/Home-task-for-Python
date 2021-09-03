from random import randint
new_list = [randint(-5, 7) for _ in range(20)]
another_list = [num for num in new_list if new_list.count(num) == 1]
print(f' My list was\n {new_list} \n and my list without repeat numbers is\n {another_list} ')
