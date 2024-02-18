# In addition I have created a process to calculate the overall largest drop from a year to another.

lowest_life_expectancy = -1
lowest_life_expectancy_country = ""
lowest_life_expectancy_year = ""
highest_life_expectancy = -1
highest_life_expectancy_country = -1
highest_life_expectancy_year = -1

average_life_expec = 0
average_quantity = 0
min_life_expec_interest = 999
max_life_expec_interest = -1
max_country_life_expec_interest = ""
min_country_life_expec_interest = ""

firstRow = True

year_of_interest = int(input("Enter the year of interest: "))

largest_drop = -1
coutry_largest_drop = ""
year_drop_before= 0
expectancy_drop_before = 0
year_drop_actual = 0
expectancy_drop_actual = 0

year_before = 0
expectancy_before = 0
country_before = ""

with open("w6Milestone_life-expectancy.csv") as csv_data:
    for line in csv_data:
        if(firstRow):
            firstRow = False
            continue #move to the next iteration
        
        line = line.strip()
        columns = line.split(",")
        life_expectancy = float(columns[3])
        life_expectancy_year = int(columns[2])
        life_expectancy_country = columns[0]
        
        #### LARGEST DROP ##########################
        if(life_expectancy_country == country_before):
            drop = float(expectancy_before - life_expectancy)
            if(drop >0):
                if(drop > largest_drop):
                    largest_drop = drop
                    coutry_largest_drop = life_expectancy_country
                    expectancy_drop_before= expectancy_before
                    expectancy_drop_actual = life_expectancy
                    year_drop_actual = life_expectancy_year
                    year_drop_before = year_before
                
            year_before = life_expectancy_year
            country_before = life_expectancy_country
            expectancy_before = life_expectancy     
        else:
            country_before = life_expectancy_country
            year_before = life_expectancy_year
            expectancy_before = life_expectancy


        ############################################

        if(lowest_life_expectancy == -1):
            lowest_life_expectancy = life_expectancy
            lowest_life_expectancy_country = life_expectancy_country
            lowest_life_expectancy_year = life_expectancy_year

            highest_life_expectancy = life_expectancy
            highest_life_expectancy_country = life_expectancy_country
            highest_life_expectancy_year = life_expectancy_year

        
        if(life_expectancy < lowest_life_expectancy):
            lowest_life_expectancy = life_expectancy
            lowest_life_expectancy_country = life_expectancy_country
            lowest_life_expectancy_year = life_expectancy_year
        
        if(life_expectancy > highest_life_expectancy):
            highest_life_expectancy = life_expectancy
            highest_life_expectancy_country = life_expectancy_country
            highest_life_expectancy_year = life_expectancy_year

        if(life_expectancy_year == year_of_interest):
            average_life_expec += life_expectancy
            average_quantity += 1

            if(life_expectancy < min_life_expec_interest):
                min_life_expec_interest = life_expectancy
                min_country_life_expec_interest = life_expectancy_country

            if(life_expectancy > max_life_expec_interest):
                max_life_expec_interest = life_expectancy
                max_country_life_expec_interest = life_expectancy_country


        


# print(f"\nThe lowest life expectancy is: {lowest_life_expectancy:.2f}")
# print(f"\nThe highest life expectancy is: {highest_life_expectancy:.2f}")
            
print(f"\nThe overall max life expectancy is: {highest_life_expectancy:.3f} from {highest_life_expectancy_country} in {highest_life_expectancy_year}.")
print(f"\nThe overall min life expectancy is: {lowest_life_expectancy:.2f} from {lowest_life_expectancy_country} in {lowest_life_expectancy_year}")

print(f"\n\nThe overall largest drop of life exppectancy is {largest_drop:.3f} in {coutry_largest_drop} from the years {year_drop_before} with {expectancy_drop_before:.3f} "
      f"to {year_drop_actual} with {expectancy_drop_actual:.3f}.")

print(f"\n\nFor the year {year_of_interest}:")
average_life_expec = float(average_life_expec/average_quantity)
print(f"The average life expectancy across all countries was {average_life_expec:.2f}")
print(f"The max life expectancy was in {max_country_life_expec_interest} with {max_life_expec_interest:.2f}")
print(f"The min life expectancy was in {min_country_life_expec_interest} with {min_life_expec_interest:.3f}")



