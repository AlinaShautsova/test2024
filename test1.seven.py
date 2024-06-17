"""Module contains a solution to the task: seven."""


def solution(s, n):
    """Function solution."""
    beginning = s[:n]
    reversed_beginning = beginning[::-1]
    end = reversed_beginning[1:]
    return beginning + end


string = "abcdefghijklmnopqrstuvwxyz"
assert solution(string, 1) == "a"
assert solution(string, 2) == "aba"
assert solution(string, 3) == "abcba"
assert solution(string, 4) == "abcdcba"
