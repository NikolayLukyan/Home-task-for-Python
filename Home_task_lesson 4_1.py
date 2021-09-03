from sys import argv


def money_you_earn():
    try:
        time_you_work, your_scale, your_surcharge = map(float, argv[1:])
        print(f'You earn = {time_you_work * your_scale + your_surcharge}, money')
    except ValueError:
        print('You must enter three numbers. It is forbidden to enter string or empty space')


money_you_earn()
