from functools import reduce


def multi(num_1, num_2):
    return num_1 * num_2


new_list = [sub for sub in range(100, 1001, 2)]
print(f' My list was\n {new_list} \n the result of multiplication is\n {reduce(multi, new_list)}\n ')
