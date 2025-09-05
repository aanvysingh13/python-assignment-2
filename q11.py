# given string
text = "Emma is a good friend. Emma likes Python. Emma is smart."

# substring to search
substring = "Emma"

# count occurrences
count = 0
for i in range(len(text) - len(substring) + 1):
    if text[i:i+len(substring)] == substring:
        count += 1

print(f'The substring "{substring}" appears', count, "times.")