import random

import Car

cars = []

for i in range(10):
    cars.append(Car.Car(f"ABC-{i}", random.randint(100,200)))

while(True):
    current_car = i
    for i in range(10):
        cars[i].accelerate(random.randint(-10,15))
        cars[i].move(1)
        if(cars[i].traveled_distance>=10000):
            current_car = i
            break
    if (cars[current_car].traveled_distance >= 10000):
        print(f"Auto {cars[current_car].license_plate} voitti")
        break

for i in range(10):
    print(cars[i])