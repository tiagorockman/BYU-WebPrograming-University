def main():
  try:
      # Create and print a list named fruit.
      fruit_list = ["pear", "banana", "apple", "mango"]
      print(f"original: {fruit_list}")
      #Add code to reverse and print fruit_list.
      fruit_list = reverse_list(fruit_list)
      print(f"reverse: {fruit_list}")
      #Add code to append "orange" to the end of fruit_list and print the list. 
      fruit_list.append('orange')
      print(fruit_list)
      # Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
      apple_location= fruit_list.index('apple')
      fruit_list.insert(apple_location, 'cherry')
      print(fruit_list)
      #Add code to remove "banana" from fruit_list and print the list.
      banana_location = fruit_list.index('banana')
      fruit_list.pop(banana_location)
      print(fruit_list)
      #Add code to pop the last element from fruit_list and print the popped element and the list.
      pop_item = fruit_list[len(fruit_list)-1]
      fruit_list.pop(len(fruit_list)-1)
      print(f"popped: " + pop_item)
      print(fruit_list)
      #Add code to sort and print fruit_list.
      fruit_list.sort()
      print(f"Sorted: {fruit_list}")
      #Add code to clear and print fruit_list.
      fruit_list.clear()
      print(f"Cleanned: {fruit_list}")
  except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")

def reverse_list(list):
  reverse_list = []
  last_item = len(list)
  for _ in range(len(list)):
    reverse_list.append(list[last_item - 1])
    last_item = last_item - 1
  return reverse_list


if __name__ == "__main__":
    main()