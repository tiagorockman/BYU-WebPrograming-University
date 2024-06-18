import math
from datetime import datetime

def tire_volume(w, a, d):
    v = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000
    return v

def write_volume_txt(date, w, a, d, v):
    with open("volumes.txt", "a") as file:
        file.write(f"{date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}\n")


# Milestone: Tire Volume

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspec_ratio = int(input("Enter the aspect ration of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the whell in  inches (ex 15): "))


volume = tire_volume(width, aspec_ratio, diameter)
print(f"The approximate volume is {volume:.2f} liters")

current_date = datetime.now()
write_volume_txt(current_date, width, aspec_ratio,diameter, volume)
