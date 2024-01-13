#Working with Strings
words = "the cat IN THE hat"

print("capitalize: " + words.capitalize());

print("title: " + words.title());

print("upper: " + words.upper());

print("lower: " + words.lower());

print(f"count('t'): {str(words.count("t"))}");

print(f"lower().count('t'): {str(words.lower().count("t"))}");

#Concatenation String
print("Concatenation String")
first_name = "Tiago"
last_name = "Neves"
output = "Hello, {} {}".format(first_name, last_name)
print(output);
output = "Hello, {0} {1}".format(first_name, last_name)
print(output);
output = f"Hello, {first_name} {last_name}"
print(output);

#Program

print("\n\n")
first_name = input("What is your first name?")
last_name = input("What is your last name?")

print(f"Your name is {last_name}, {first_name} {last_name}.")

print("Titled")
print(f"Your name is {last_name.title()},  {first_name.title()} {last_name.title()}.")