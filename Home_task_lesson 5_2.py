with open('my_file_2.txt', 'r', encoding='utf-8') as my_favorite:
    use = [f'{line}. {count.strip()} - {len(count.split())} words'
           for line, count in enumerate(my_favorite, 1)]
    print(*use, f'In this file you have - {len(use)} strings.', sep='\n')
