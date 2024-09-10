from Car import ElectricVehicle,GasolineVehicle

ev = ElectricVehicle("ABC-15", 180,52.5)
gv = GasolineVehicle("ACD-123", 165,32.3)

ev.current_speed = ev.top_speed
gv.current_speed = gv.top_speed

ev.move(3)
gv.move(3)

print(f"Sähköauto mittarilukema: {ev.traveled_distance}")
print(f"Polttomoottori mittarilukema: {gv.traveled_distance}")
