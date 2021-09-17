class Date(object):

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        print('Your date is', f'{day:02}.', 'Your month is', f'{month:02}. ', 'Your year is', f'{year:04}.')


    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if 0 < day <= 31:
            if 0 < month <= 12:
                if 2100 > year >= 0:
                    print(f'You enter correct date', date_as_string)
                else:
                    print('You enter year', f'{year:04}.', 'It is a wrong number for year.')
            else:
                print('You enter', f'{month:02}.', 'It is a wrong number for a month.')
        else:
            print('You enter', f'{day:02}.', 'It is a wrong number for a day.')


a = '4-8-2020'
b = '35-2-2000'
date2 = Date.from_string(a)
check_date = Date.is_date_valid(a)
date3 = Date.from_string(b)
check_date_2 = Date.is_date_valid(b)
