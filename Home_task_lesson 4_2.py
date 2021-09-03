from random import randint

new_list = [randint(0, 10000) for _ in range(0, randint(0, 25))]
next_more_previous = [new_list[num] for num in range(1, len(new_list)) if new_list[num] > new_list[num - 1]]
print(next_more_previous)
print(new_list)