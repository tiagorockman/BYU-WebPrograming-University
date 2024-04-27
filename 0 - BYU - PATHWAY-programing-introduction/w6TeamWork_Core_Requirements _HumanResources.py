with open("hr_system.txt") as employees_data:
    for data in employees_data:
        data = data.split()
        # data = 'Alexia 1913 Engineer 84000'
        # data = ['Alexia', '1913', 'Engineer', '84000']
        name = data[0]
        role = data[2]
        print(f"Name: {name}, Title: {role}")