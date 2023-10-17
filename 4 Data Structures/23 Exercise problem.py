# find the most repeated character in the text

sentence = 'This is a common interview question'

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(char_frequency)

# sorting the dict
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)

print(char_frequency_sorted[0])

final = [*char_frequency_sorted[0]]
print('char:', final[0])
print('Repeated:', final[1], 'times')


charTime = {}

for ch in sentence:
    if ch in charTime:
        charTime[ch] += 1
    else:
        charTime[ch] = 1

print(charTime)
