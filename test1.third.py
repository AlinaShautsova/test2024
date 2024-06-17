"""Module contains a solution to the task: third."""


def count_and_return(a):
    """Return number of capital and lowercase letters."""
    upper_count = 0
    lower_count = 0

    for char in a:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count


string = "The quick Brow Fox"
upper_case, lower_case = count_and_return(string)
print(f"Upper case characters: {upper_case}, Lower case characters:"
      f" {lower_case}")
