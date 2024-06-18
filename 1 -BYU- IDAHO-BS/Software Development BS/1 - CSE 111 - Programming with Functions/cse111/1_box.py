import math

num_items = int(input(f"Enter the number of items: "))
items_per_box = int(input(f"Enter the number of items per box: "))

# Compute the number of boxes by dividing
# and then calling the math.ceil function.
num_boxes = math.ceil(num_items / items_per_box)

print(f"For {num_items} items, packing {items_per_box}"
    f" items in each box, you will need {num_boxes} boxes.")