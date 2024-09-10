from Car import Car

car = Car("ABD-123", 142)

print(f"Rekisterikilpi = {car.license_plate}\nHuippunopeus   = {car.top_speed}")

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"\nNykyinen nopeus = {car.current_speed}")
car.accelerate(-200)
print(f"Nykyinen nopeus = {car.current_speed}")
