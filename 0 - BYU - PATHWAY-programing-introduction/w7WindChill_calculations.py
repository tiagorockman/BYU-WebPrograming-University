def calculate_wind_chill(temperature, wind_speed):
    calculation_= 35.74 + 0.6215 * temperature - 35.75*wind_speed**0.16 + 0.4275*temperature*wind_speed**0.16
    return calculation_

def celsius_to_fahrenheit(celsius_temperature):
    celsius_temperature = celsius_temperature * 9/5
    return celsius_temperature + 32



temperature = int(input("What is the temperature? "))
weather_measure = input("Fahrenheior Celsius (F/C)? ")

if(weather_measure.upper() == "C"):
    temperature = celsius_to_fahrenheit(temperature)

for wind_speed in range(5,61,5):
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    print(f"At temperature {float(temperature):.1f}F, and wind speed {wind_speed} mph, the windchill is: {float(wind_chill):.2f}F")