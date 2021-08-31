def div(a_1, a_2):
    try:
        a_1, a_2 = int(a_1), int(a_2)
        div_result = a_1 / a_2
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return 'Division by null forbidden'
    return round(div_result, 4)


print(div(input('Введите первое число: '), input('Введите свое второе число: ')))
