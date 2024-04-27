with open("w6Working_with_file.txt") as course_file:
    for line in course_file:
        line = line.strip() #remove whitespaces and line breakers
        columns = line.split(",")
        course_name = columns[0]
        grade = float(columns[1])
        
        bonus_grade = grade + 3

        print(f"{course_name} - Grade: {grade}, after bonus: {bonus_grade}")