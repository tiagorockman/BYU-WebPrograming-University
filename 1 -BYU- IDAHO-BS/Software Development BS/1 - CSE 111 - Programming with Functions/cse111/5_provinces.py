def main():
    list = read_file()
    length = len(list)
    print(list)
    print(f"First Item: {list[0]}")
    print(f"Last Item: {list[length-1]}")
    list.pop(0)
    print("remove first item")
    list.pop() 
    print("remove last item")
    print(f"First Item: {list[0]}")
    length = len(list)
    print(f"Last Item: {list[length-1]}")
    print("Replace all occurrences of 'AB' in the list with 'Alberta'.")
    for i in range(len(list)):
        if list[i] == "AB":
            list[i] = "Alberta"
    print(list)
    print("Count the number of elements that are 'Alberta' and print that number.")
    count = list.count("Alberta")
    print(f"Alberta occurs {count} times in the modified list")

def read_file():
    file_text = []
    with open("provinces.txt", "rt") as text_file:
        for line in text_file:
            line_without_espace = line.strip()
            file_text.append(line_without_espace)
    
    return file_text

if __name__ == "__main__":
    main()