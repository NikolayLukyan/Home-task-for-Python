class Cell:

    def __init__(self, elem):
        self.elem = elem

    def make_order(self, rows):
        return '\n'.join(['' * rows for _ in range(self.elem // rows)]) + '\n' + '' * (self.elem % rows)

    def __str__(self):
        return f'{self.elem}'

    def __add__(self, other):
        print('Sum of cells is')
        return Cell(self.elem + other.elem)

    def __sub__(self, other):
        print('Subtraction of cells is')
        return Cell(self.elem - other.elem) if self.elem - other.elem > 0 \
            else 'In the first cell You have smaller elements then in the second so subtraction is not available.'

    def __mul__(self, other):
        print('Multiplication of cells is')
        return Cell(self.elem * other.elem)

    def __floordiv__(self, other):
        print('Integer division of cells is')
        return Cell(self.elem // other.elem)


cell_1 = Cell(17)
cell_2 = Cell(5)

print(cell_2.make_order(2))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
