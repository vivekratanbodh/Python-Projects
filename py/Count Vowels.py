#20210616

vowels = 'aeiou'
text = input('Text Line')

text = text.casefold()

count = {}.fromkeys(vowels,0)

for char in text:
    if char in count:
        count[char] += 1
print(count)
