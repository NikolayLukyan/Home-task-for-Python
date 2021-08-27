list_with_my_information = [(1.2, 5.8, 9), 2, 15, ('inf', 'more'), {1: 'name', 2: 'surname'}, {2, 12, 123}, range(3),
                            (-5 + 6j), True, 'String', [7, 14, 28], TypeError]
for i, item in enumerate(list_with_my_information, 1):
    print(f'({i}, {item} - {type(item)})')
