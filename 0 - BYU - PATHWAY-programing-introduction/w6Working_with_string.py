#Split String
colors = "red green yellow blue"

colors_part = colors.split() #split the colors by Whitespace

print(colors)
print(colors_part)

colors_byE = colors.split("e")
print(colors_byE)

#Working with WhiteSpace
name = "Brother Burton            "

clean_name = name.strip() #remove whitespace

print(f"name----{name}----")
print(f"clean name----{clean_name}----")