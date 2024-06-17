"""Module contains a solution to the task: first."""


print("Свяжите переменную с любой строкой, состоящей не менее чем из 15"
      " символов.")
first_string = "Hello this wonderful world."
print("String:", first_string)

print("Извлеките из строки первый символ")
first_char = first_string[0]
print("First char:", first_char)

print("Извлеките из строки последний символ")
last_char = first_string[-1]
print("Last char:", last_char)

print("Извлеките из строки третий с начала")
third_char = first_string[2]
print("Third char:", third_char)

print("Извлеките из строки третий с конца")
third_last_char = first_string[-3]
print("Third last char:", third_last_char)

print("Измерьте длину вашей строки")
first_string_length = len(first_string)
print("First_string_length:", first_string_length)

print("Переверните строку")
reversed_string = first_string[::-1]
print("Reversed_string:", reversed_string)

print("Извлеките первые восемь символов")
first_eight_chars = first_string[:8]
print("First_eight_chars:", first_eight_chars)
