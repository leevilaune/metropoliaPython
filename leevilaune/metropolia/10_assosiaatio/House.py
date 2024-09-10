import Elevator

class House:

    elevators = []

    def __init__(self, bottom_floor,top_floor, elevators_no):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators_no = elevators_no
        self.generate_elevators(bottom_floor,top_floor,elevators_no)

    def generate_elevators(self, bottom, top,no):
        for i in range(no):
            self.elevators.append(Elevator.Elevator(bottom,top))
        print(f"Hissejä luotu: {len(self.elevators)}")

    def move_elevator(self, elevator_no, to_floor):
        print(f"Hissi {elevator_no}: {self.elevators[elevator_no].move_to_floor(to_floor)}")

    def fire_alarm(self):
        print(f"Palohälytys!! Siirretään hissit pohjakerrokseen")
        for i in range(len(self.elevators)):
            self.move_elevator(i,0)
