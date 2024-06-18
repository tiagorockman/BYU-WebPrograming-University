"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("How old are you? "))
max_heart_rate = 220
max_heart_rate_per_min = max_heart_rate - age
min = int((max_heart_rate_per_min * 65)/100)
max = int((max_heart_rate_per_min * 85)/100)

print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {min:.0f} and {max:.0f}")
print("beats per minute.")