
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = 0

    def move_to_floor(self,to):
        if self.top_floor >= to >= self.bottom_floor:
            self.current_floor = to
            return f"Hissi on kerroksessa {self.current_floor}"
        else:
            return f"Ei voida siirtyä kerrokseen {to}"

    def move_up(self):
        if self.current_floor+1<=self.top_floor:
            self.current_floor += 1
        else:
            print("Ei voida liikkua korkeinta kerrosta ylemmäksi")
        print(f"Hissi on kerroksessa {self.current_floor}")

    def move_down(self):
        if self.current_floor - 1 >= self.top_floor:
            self.current_floor -= 1
        else:
            print("Ei voida liikkua alinta kerrosta alemmaksi")
        print(f"Hissi on kerroksessa {self.current_floor}")
