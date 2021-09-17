class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_mass(self, weight=25, thickness=7):
        return f'{self._length} m * {self._width} m *{weight} kg * {thickness} sm = ' \
               f'{(self._length * self._width * weight * thickness) / 1000} t'


road_1 = Road(2500, 25)
print(road_1.get_full_mass())