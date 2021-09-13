from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, elem):
        self.elem = elem

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, another):
        Clothes.result += self.consumption + another.consumption
        return Suit(0)

    def __str__(self):
        resu = Clothes.result
        Clothes.result = 0
        return f'{resu}'


class Suit(Clothes):
    @property
    def consumption(self):
        return round((2 * self.elem + 0.3) / 100)


class Coat(Clothes):
    @property
    def consumption(self):
        return round((self.elem / 6.5) + 0.5)


coat = Coat(50)
suit = Suit(176)
print(f'If You want to sew coat and two suit, then You need ', suit + suit + coat, ' meters of material')
