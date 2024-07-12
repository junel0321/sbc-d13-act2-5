text = input("Enter a sentence: ")
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
                  "+", "[", "{", "]", "}", "\\", "|", ";", ":", ",", "<", ".", ">", "/", "?", "`", "~"]

# Replace the special characters with space
for char in special_chars:
    text = text.replace(char, " ")

# Split inputed text by spaces
tokens = text.split()

# change the double quotes and commas
output = ""
for token in tokens:
    if output:
        output += ", "
    output += '"' + token + '"'

print(output)
