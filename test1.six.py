"""Module contains a solution to the task: seven."""


def count_file_contents(filename):
    file = open(filename, 'r', encoding='utf-8')
    content = file.read()
    file.close()

    lines = content.split('\n')
    num_lines = len(lines)
    num_words = len(content.split())
    num_letters = len([char for char in content if char.isalpha()])

    summary = (f"\nStatistics:\n"
               f"Number of lines: {num_lines}\n"
               f"Number of words: {num_words}\n"
               f"Number of letters: {num_letters}\n")

    file = open(filename, 'a', encoding='utf-8')
    file.write(summary)
    file.close()

    print(summary)


filename = 'example.txt'
count_file_contents(filename)
