while True:
    days = 1
    start_distance = float(input("Введите длину первой дистанции (значение больше 0): "))
    finish_distance = float(input("Введите финишную дистанцию в км (больше 0): "))
    if start_distance <= 0 or finish_distance < 0:
        print(f'Дистанции должны быть больше 0. Стартовое значение не может быть 0')
    else:
       while start_distance < finish_distance:
           start_distance = start_distance + start_distance * 0.1
           days = days + 1
       print(f'спортсмен достигнет требуемого результата {finish_distance} на {days} день тренировок.')
       break
