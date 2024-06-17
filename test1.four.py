"""Module contains a solution to the task: four."""


def add_number(number):
    """Add one to a number and returns a list """
    number.reverse()

    carry = 1

    for i in range(len(number)):
        number[i] += carry
        if number[i] > 9:
            carry = 1
            number[i] = 0
        else:
            carry = 0
            break
    if carry == 1:
        number.append(1)
    return number[::-1]


assert add_number([9]) == [1, 0]
assert add_number([1, 2, 3]) == [1, 2, 4]
assert add_number([1, 1, 9]) == [1, 2, 0]
assert add_number([9, 9, 9]) == [1, 0, 0, 0]
