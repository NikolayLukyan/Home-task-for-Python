with open('my_file_5.txt', 'r', encoding='utf-8') as my_favorite:
    dict_of_employees = {line.split()[0]: float(line.split()[1]) for line in my_favorite}
    print(f'The average salary in this firm is {round(sum(dict_of_employees.values()) / len(dict_of_employees), 3)}\n'
          f'Employees who have salary less than 20.000 {[el[0] for el in dict_of_employees.items() if el[1] < 20000]}')
