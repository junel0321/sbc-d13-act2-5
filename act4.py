text = input("Enter a word: ")

prefixes = ["un", "re", "pre", "dis", "mis", "ex", "non", "anti", "post", 
    "mid", "sub", "super", "inter", "over", "under", "semi", "co", 
    "para", "hyper", "multi"]
suffixes = ["ed", "ing", "ly", "able", "ible", "tion", "sion", "ment", "ness", 
    "ful", "less", "ist", "er", "or", "ism", "ive", "ative", "ize", "ise", 
    "al", "ial", "ical", "ic", "ate", "ize"]

# Check for prefixes
for prefix in prefixes:
    if text.startswith(prefix):
        text = "*" * len(prefix) + text[len(prefix):]

# Check for suffixes
for suffix in suffixes:
    if text.endswith(suffix):
        text = text[:-len(suffix)] + "*" * len(suffix)

print(text)
