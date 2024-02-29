def list_of_numbers_from_input():
    # Get a list of numbers as input from a user
    input_string = input('Enter elements of a list separated by space ')
    print("\n")
    user_list = input_string.split()
    # print list
    print('list: ', user_list)

    # convert each item to int type
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])

    # Calculating the sum of list elements
    print("Sum = ", sum(user_list))

def list_of_numbers_from_input_range():
    # Input a list using input() and range() function
    list1 = []
    n = int(input("Enter the list size "))

    print("\n")
    for i in range(0, n):
        print("Enter item at index", i, )
        item = str(input())
        list1.append(item)
    print("User list is ", list1)

def list_of_numbers_from_input_range2():
    # Input a list using a list comprehension
    n = int(input("Enter the size of the list "))
    print("\n")
    num_list = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:n]

    print("User list: ", num_list)

def list_of_numbers_from_input_using_map():
    # Input a list using the map function
    n = int(input("Enter the size of list : "))
    print("\n")
    numList = list(map(float, input("Enter the list numbers separated by space ").strip().split()))[:n]
    print("User List: ", numList)

def list_of_strings_from_input():
    # Get a list of strings as an input from a user
    input_string = input("Enter all family members name separated by space  ")
    # Split string into words
    family_list = input_string.split(" ")

    print("\n")
    # Iterate a list
    print("Printing all family member names")
    for name in family_list:
        print(name)

def nested_list_from_input():
    # Accept a nested list as input
    # accept nested list from user
    list_size = int(input("Enter the number of sub list "))

    print("\n")
    final_list = [[int(input("Enter single number and press enter: ")) for _ in range(list_size)] for _ in range(list_size)]
    print("List is", final_list)


def convert_string_input_to_number_to_check_if_number():
    # Convert string input to int or float to check if it is a number
    def check_user_input(input):
        try:
            # Convert it into integer
            val = int(input)
            print("Input is an integer number. Number = ", val)
        except ValueError:
            try:
                # Convert it into float
                val = float(input)
                print("Input is a float  number. Number = ", val)
            except ValueError:
                print("No.. input is not a number. It's a string")


    input1 = input("Enter your Age ")
    check_user_input(input1)

    input2 = input("Enter any number ")
    check_user_input(input2)

    input2 = input("Enter the last number ")
    check_user_input(input2)


def check_if_input_is_number_or_string():
    # Use string isdigit() method to check user input is number or string
    def check_is_digit(input_str):
        if input_str.strip().isdigit():
            print("User input is Number")
        else:
            print("User input is string")


    num1 = input("Enter number and hit enter")
    check_is_digit(num1)

    num2 = input("Enter number and hit enter")
    check_is_digit(num2)


def only_accept_number_as_input():
    # Only accept a number as input
    while True:
        num = input("Please enter a number ")
        try:
            val = int(num)
            print("Input is an integer number.")
            print("Input number is: ", val)
            break;
        except ValueError:
            try:
                float(num)
                print("Input is an float number.")
                print("Input number is: ", val)
                break;
            except ValueError:
                print("This is not a number. Please enter a valid number")


def check_if_input_number_is_pos_or_neg():
    # Practice Problem: Check user input is a positive number or negative
    user_number = input("Enter your number ")

    print("\n")
    try:
        val = int(user_number)
        if val > 0:
            print("User number is positive ")
        else:
            print("User number is negative ")
    except ValueError:
        print("No.. input string is not a number. It's a string")
