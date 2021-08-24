user_number = input("Введите свое целое число больше 0: ")
while user_number < '0':
   print('Необходимо ввести целое число больше 0')
   user_number = input("Введите свое целое число больше 0: ")
result = int(user_number)+int(f'{user_number}{user_number}')+int(f'{user_number}{user_number}{user_number}')
print('получаемое выражение вида: ', user_number,'+',(f'{user_number}{user_number}'),'+',(f'{user_number}{user_number}{user_number}'),'=', result )