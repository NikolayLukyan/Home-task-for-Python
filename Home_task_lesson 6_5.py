class Stationery:

    def __init__(self, title='You can write with it'):
        self.title = title

    def start(self):
        print(f' You are starting  to write with {self.title} ink.')


class Pen(Stationery):

    def start(self):
        print(f' You are starting  to write with {self.title} pen.')


class Pencil(Stationery):

    def start(self):
        print(f' You are starting  to write with {self.title} pencil.')


class Stylus(Stationery):

    def start(self):
        print(f' You are starting  to write with {self.title} stylus.')


st = Stationery('black')
pe = Pen('yellow')
pen = Pencil('red')
sty = Stylus('blue')

my_list = [st, pe, pen, sty]
for i in my_list:
    i.start()
    print()
