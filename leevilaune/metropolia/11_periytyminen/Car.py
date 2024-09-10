class Car:
    def __init__(self,license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def accelerate(self, amount):
        self.current_speed += amount
        if((self.current_speed+amount)>self.top_speed):
            self.current_speed = self.top_speed
        elif((self.current_speed+amount)<0):
            self.current_speed = 0

    def move(self, hours):
        self.traveled_distance += self.current_speed*hours


    def __str__(self):
        return f"Car(rekisteri_numero:{self.license_plate}  huippu_nopeus:{self.top_speed}km/h  nykyinen_nopeus:{self.current_speed:03d}km/h  kuljettu_matka:{self.traveled_distance:05d}km)"

class ElectricVehicle(Car):
    def __init__(self, license_plate, top_speed, battery_capacity):
        super().__init__(license_plate,top_speed)
        self.battery_capacity = battery_capacity

class GasolineVehicle(Car):
    def __init__(self,license_plate, top_speed, tank_capacity):
        super().__init__(license_plate,top_speed)
        self.tank_capacity = tank_capacity