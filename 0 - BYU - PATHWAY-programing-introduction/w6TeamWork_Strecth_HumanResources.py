with open("hr_system.txt") as employees_data:
    for data in employees_data:
        clean_data = data.strip()
        data = clean_data.split()
        # data = 'Alexia 1913 Engineer 84000'
        # data = ['Alexia', '1913', 'Engineer', '84000']
        name = data[0]
        role = data[2]
        id_number = int(data[1])
        salary = float(data[3])
        salary_bi_weekly = float((salary/12)/2)

        if role.lower() == "engineer":
            salary_bi_weekly += 1000

        print(f"{name} (ID: {id_number}), {role} - ${salary_bi_weekly:.2f}")