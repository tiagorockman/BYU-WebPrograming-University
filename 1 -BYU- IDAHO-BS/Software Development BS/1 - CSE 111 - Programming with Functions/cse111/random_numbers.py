import random

number_list = []

def append_random_words(word_list, quantity = 1):
    word_data_list =   ['join', 'young', 'list', 'love', 'basketball']
    for _ in range(quantity):
        word = random.choice(word_data_list)
        word_list.append(word)


def append_random_numbers(number_list, quantity = 1):
     for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded_number = round(random_number, 1)
        number_list.append(rounded_number)

def main():
     numbers = [16.2, 75.1, 52.3]
     print(numbers)
     append_random_numbers(numbers) # 1 argument
     print(numbers)
     append_random_numbers(numbers, 3) # 2 arguments
     print(numbers)
     words =  []
     append_random_words(words)
     print(words)
     append_random_words(words, 3)
     print(words)



if __name__ == "__main__":
    main()