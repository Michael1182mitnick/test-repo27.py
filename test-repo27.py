# using import random to generate random numbers between 0 and 9
# user input 3 numbers in seven columns
import random

def generate_random():
    # Generate a random number between 0 and 9
    return random.randint(0, 9)

def main():
    while True:
        for _ in range(7):
            # Prompt the user to input 3 numbers separated by spaces
            numbers_input = input("Enter 3 numbers separated by spaces (in seven columns): ")

            # Split the input string into a list of individual numbers
            numbers_list = numbers_input.split()

            # Check if the user entered exactly 3 numbers
            if len(numbers_list) != 3:
                print("Please enter exactly 3 numbers separated by spaces.")
                continue

            # Convert each number from string to integer
            try:
                numbers = [int(num) for num in numbers_list]
            except ValueError:
                print("Please enter valid integers.")
                continue

            # Check if exactly one number is odd and the other two are even, or vice versa
            if (sum(1 for num in numbers if num % 2 == 0) == 2 and sum(1 for num in numbers if num % 2 != 0) == 1) \
                    or (sum(1 for num in numbers if num % 2 != 0) == 2 and sum(1 for num in numbers if num % 2 == 0) == 1):
                # Find the opposite of each number
                opposite_numbers = [9 - num if num <= 5 else 5 - num for num in numbers]
                print("Opposite numbers:", opposite_numbers)
            # Check if the user entered 3 odd or 3 even numbers
            elif sum(1 for num in numbers if num % 2 != 0) == 3 or sum(1 for num in numbers if num % 2 == 0) == 3:
                random_numbers = [generate_random() if num % 2 == 0 else generate_random() + 5 for num in numbers]
                print("Random opposite numbers:", random_numbers)
            else:
                print("Please enter one odd number and two even numbers, or vice versa, or enter 3 odd or 3 even numbers.")
        break

if __name__ == "__main__":
    main()