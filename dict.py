# my_dict = {
#     "name": "Ali",
#     "age": 25,
#     "city": "Riyadh"
# }

# key = input("Enter the key you want to update: ")

# if key in my_dict:
#     new_value = input(f"Enter new value for '{key}': ")
#     my_dict[key] = new_value
#     print("Dictionary updated:", my_dict)
# else:
#     print(f"Key '{key}' not found in the dictionary.")
data = {
    1: "One",
    2: "Two",
    3: "Three"
}

user_input = input("Enter a number: ")

# Convert input to integer safely
if user_input.isdigit():
    number = int(user_input)
    
    if number in data:
        print(f"The value is: {data[number]}")
    else:
        print("Invalid number: not found in dictionary")
else:
    print("Invalid input: not a number")
