"""Module contains a solution to the task: second."""


def number_square():
    """Function for enter number and do number in square."""
    number = int(input("Enter number: "))
    square = number ** 2
    print(f"Number in square {number} is {square}")


def check_even_odd():
    """Function for enter number and check is even or odd."""
    number = int(input("Enter number: "))
    if number % 2 == 0:
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")


number_square()
check_even_odd()
