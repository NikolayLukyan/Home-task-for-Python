class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f'{itm:04}' for itm in line]) for line in self.data)

    def __add__(self, another):
        try:
            m = [[int(self.data[line][itm]) + int(another.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Error. Matrices have different size. You can not sum them without modification.'


m_1 = [[3, 5, 7], [12, 8, -5], [7, 9, 12]]
m_2 = [[7, 5, -2], [4, -2, -12], [7, 5, 74]]

mtr_1 = Matrix(m_1)
mtr_2 = Matrix(m_2)
sum_mtr = mtr_1 + mtr_2
print('Result summation of Matrix(m_1) and Matrix(m_2) is\n')
print(sum_mtr)
