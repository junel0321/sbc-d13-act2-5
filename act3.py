text = input("Enter a sentence: ")
quoted_letters = [f'"{char}"' for char in text]

output = ", ".join(quoted_letters)

print(output)
