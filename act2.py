input_text = input("Enter a sentence: ")

sentence_endings = {'.', '!', '?', ';', "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", ":", "/"}

sentences = []
current_sentence = ""

for char in input_text:
    current_sentence += char
    if char in sentence_endings:
        sentences.append(current_sentence.strip().replace("'", '"'))
        current_sentence = ""

if current_sentence:
    sentences.append(current_sentence.strip().replace("'", '"'))

output = ', '.join(f'"{sentence}"' for sentence in sentences)

print(output)
