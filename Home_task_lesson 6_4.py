from random import choice


class Vehicles:
    """Main vehicles"""
    direction = ['north ', 'south ', 'west ', 'east ', 'northwest', 'northeast ', 'southwest ',
                 'southeast ', 'turn around']

    def __init__(self, name, colour, speed, police=False):
        self.name = name
        self.colour = colour
        self.speed = speed
        self.is_police = police
        print(f'New vehicle is a {name} which has  colour {colour}.\n Is the vehicle a police car? {police}')

    def start(self):
        print(f' {self.name}: The car is starting a movement.')

    def stop(self):
        print(f' {self.name}: The car has stopped a movement.')

    def dir(self):
        print(f' {self.name}: The car has turned to the {choice(self.direction)}.')

    def car_speed(self):
        return f'{self.name}:The car is having  the speed equal  {self.speed}.'


class CityVehicles(Vehicles):
    """ City vehicles"""

    def car_speed(self):
        return f'{self.name}:The car is having speed equal {self.speed}. You are driving too fast!' if self.speed > 60 \
            else super().car_speed()


class WorkVehicles(Vehicles):
    """ Work vehicles"""

    def car_speed(self):
        return f'{self.name}:The car is having speed equal {self.speed}. You are driving too fast!' if self.speed > 40 \
            else super().car_speed()


class SportVehicles(Vehicles):
    """ Sport vehicles"""


class PoliceVehicles(Vehicles):
    """ Sport vehicles"""

    def __init__(self, name, colour, speed, police=True):
        super().__init__(name, colour, speed, police)


police = PoliceVehicles('Big Bob', 'black with white line', 120)
work_car = WorkVehicles('Stranger', 'red with blue lines', 60)
sport = SportVehicles('Ferrari 360', 'red', 200)
auto = CityVehicles('Ford', 'blue', 85)

my_list = [auto, sport, work_car, police]
for i in my_list:
    i.start()
    print(i.car_speed())
    i.dir()
    i.stop()
    print()
