class StoreMash:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price': self.price, 'Amount': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} amount {self.quantity}'

    def reception(self):

        try:
            unit = input(f'Enter model ')
            unit_p = int(input(f'Enter price per unit '))
            unit_q = int(input(f'Enter amount '))
            unique = {'Model': unit, 'Price per unit': unit_p, 'Amount': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'List now is -\n {self.my_store}')
        except:
            return f'Incorrect enter'

        print(f'For exit - Q, Continue - Enter')
        q = input(f'---> ')
        if q == q.lower():
            self.my_store_full.append(self.my_store)
            print(f'All warehouse -\n {self.my_store_full}')
            return f'Exit'
        else:
            print(StoreMash.reception(self))


class Printer(StoreMash):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMash):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Multifuncdevice(StoreMash):
    def to_copy(self):
        return f'to copy smth  {self.numb} times'


unit_1 = Printer('Samsung', 85000, 2, 3)
unit_2 = Scanner('HP', 35000, 7, 12)
unit_3 = Multifuncdevice('Xerox', 28000, 5, 278)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copy())
