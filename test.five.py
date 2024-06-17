"""Module contains a solution to the task: five."""


def is_palindrome(a):
    """Checks whether the palindrome is palindrome or not."""
    a = a.lower().replace('', "")
    return a == a[::-1]


user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
