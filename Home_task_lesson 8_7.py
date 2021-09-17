class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'The result of summarizing z1 and z2 is', f'{self.a + other.a}', ' +', f'{self.b + other.b}', ' * i')
        return f'Summ = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'The result of multiplication z1 on z2 is Mult =', f'{self.a * other.a - (self.b * other.b)}+'
                                                                  f'{self.b * other.a + self.a * other.b}', '*i')
        return f'Mult =' f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b}*i'

    def __str__(self):
        return f' Complex= {self.a} + {self.b} *i'


z_1 = ComplexNumber(24, 12)
z_2 = ComplexNumber(5, -7)
ComplexNumber(2, 1).__add__(ComplexNumber(3, 4))
ComplexNumber(2, 1).__mul__(ComplexNumber(3, 4))
print('Your first comlex number is', z_1, 'Your second comlex number is', z_2)
print(z_1 + z_2)
print(z_1 * z_2)
