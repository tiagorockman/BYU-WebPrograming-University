import math
from datetime import datetime

def tire_volume(w, a, d):
    v = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000
    return v

def write_volume_txt(date, w, a, d, v):
    with open("volumes.txt", "a") as file:
        file.write(f"{date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}\n")

# LIST of Price - Dictionary
TIRE_PRICE = [{"w": 195, "a": 65, "d": 15, "p": 88.89}, 
              {"w": 185, "a": 50, "d": 14, "p": 79.00},
              {"w": 205, "a": 50, "d": 15, "p": 100.90},
              {"w": 205, "a": 60, "d": 15, "p": 395.50}
                ]

# Milestone: Tire Volume

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspec_ratio = int(input("Enter the aspect ration of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the whell in  inches (ex 15): "))


volume = tire_volume(width, aspec_ratio, diameter)
print(f"The approximate volume is {volume:.2f} liters")

current_date = datetime.now()
write_volume_txt(current_date, width, aspec_ratio,diameter, volume)

# Print tire's price

for line in TIRE_PRICE:
    if(line["w"]==width and line["a"]==aspec_ratio and line["d"]==diameter):
        price = line["p"]
        print(f"The tire's price is: {price:.2f}")
        break