#Transportation sugession as pr the distance
distance = int(input('Enter distance in kilometer:'))

if distance < 3:
    transportation = "Walk"

elif distance > 3 and distance < 15:
    transportation = "Bike"
else:
    transportation = "Car"

print(f"Your tranportation medium should be \"{transportation}\"")
