import random


class Competition:
    def __init__(self,name, length_km, cars):
        self.name = name
        self.length_km = length_km
        self.cars = cars

    def hour_forward(self):
        for c in self.cars:
            c.accelerate(random.randint(-10, 15))
            c.move(1)
            
    def print_standings(self):
        for c in self.cars:
            print(c)

    def is_finished(self):
        for c in self.cars:
            if c.traveled_distance>=self.length_km:
                return True
        return False