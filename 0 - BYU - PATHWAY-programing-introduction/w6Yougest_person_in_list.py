
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_person = ""
youngest_age = -1

for person in people:
    person = person.split()
    age = int(person[1])
    if(youngest_age == -1):
        youngest_person = person[0]
        youngest_age = age

    if(age < youngest_age):
        youngest_person = person[0]
        youngest_age = age

print(f"The youngets person is: {youngest_person} who is {youngest_age} years old.")