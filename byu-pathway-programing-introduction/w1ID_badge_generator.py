print("Please enter the following information:\n\n")
first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id = input("ID Number: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
started_month = input("Started month: ")
training = input("Training (Yes/No) : ")


print("\n\nThe ID Card is:")
print("---------------------------")
print(f"{first_name.upper()}, {last_name.capitalize()}")
print(f"{job_title.capitalize()}")
print(f"ID: {id}")
print(f"\n\n{email.lower()}")
print(f"{phone_number}\n\n")

#this :<25 makes a distance from the other property     
print(f"Hair: {hair_color.capitalize():<25} Eyes: {eye_color.capitalize()}") 
print(f"Month: {started_month.capitalize():<25} Training: {training.capitalize()}")
print("---------------------------")


# python w1ID_badge_generator.py
# Sample Data
# DOE, Jane
# Chief Software Architect
# ID: 83-23821

# janedoe@email.com
# (208) 555-1234

# Hair: Brown           Eyes: Blue
# Month: September      Training: Yes