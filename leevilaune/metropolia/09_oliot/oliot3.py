from Car import Car

car = Car("ABC-123",142)

car.accelerate(60)
car.move(1.5)

print(f"Kuljettu matka = {car.traveled_distance}")