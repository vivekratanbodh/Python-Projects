text=input('Text Line')
vowels = 'aeiou'
text = text.casefold()

count = {}.fromkeys(vowels,0)

for char in text:
    if char in count:
        count[char]+=1
print(count)