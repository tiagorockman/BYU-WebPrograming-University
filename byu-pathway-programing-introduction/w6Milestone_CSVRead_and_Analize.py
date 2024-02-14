

lowest_life_expectancy = -1
highest_life_expectancy = -1
firstRow = True

with open("w6Milestone_life-expectancy.csv") as csv_data:
    for line in csv_data:
        if(firstRow):
            firstRow = False
            continue #move to the next iteration

        columns = line.split(",")
        life_expectancy = float(columns[3])

        if(lowest_life_expectancy == -1):
            lowest_life_expectancy = life_expectancy
            highest_life_expectancy = life_expectancy
        
        if(life_expectancy < lowest_life_expectancy):
            lowest_life_expectancy = life_expectancy
        
        if(life_expectancy > highest_life_expectancy):
            highest_life_expectancy = life_expectancy


print(f"The lowest life expectancy is: {lowest_life_expectancy:.2f}")
print(f"The highest life expectancy is: {highest_life_expectancy:.2f}")
