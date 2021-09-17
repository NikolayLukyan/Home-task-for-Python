from time import sleep
from itertools import cycle


class TrafficLight:
    __colour = ['   ', [7, 2, 4], ['\033[41m\033[2m', '\033[43m\033[1m', '\033[42m\033[1m']]

    def start(self):
        my_traf = ['', '']
        for i in cycle((0, 1, 2)):
            my_traf[1] = self.__colour[2][i]
            print(f'\r({my_traf[int(i == 0)]}{self.__colour[0]}\033[0m)'
                  f'({my_traf[int(i == 1)]}{self.__colour[0]}\033[0m)'
                  f'({my_traf[int(i == 2)]}{self.__colour[0]}\033[0m)', end='')
            sleep(self.__colour[1][i])


traff = TrafficLight()
traff.start()
