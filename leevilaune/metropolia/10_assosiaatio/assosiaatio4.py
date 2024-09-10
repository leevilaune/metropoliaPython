import random

from Competition import Competition
from Car import Car

cars = []
for i in range(10):
    cars.append(Car(f"ABC-{i}", random.randint(100,200)))

competition = Competition("Suuri romuralli",8000,cars)

index = 0
while True:
    competition.hour_forward()
    if competition.is_finished():
        break
    index+=1
    if index%10==0:
        print(f"\nNykyinen tilanne {index}h")
        competition.print_standings()

print("\nLoppu tilanne")
competition.print_standings()