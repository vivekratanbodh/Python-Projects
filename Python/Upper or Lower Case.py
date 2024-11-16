char = input("Enter Text")

if(char >= 'A' and char <= 'Z'):
    print(char," - is in Upper Case")
elif(char >= 'a' and char <= 'z'):
    print(char," - is in Lower Case")
else:
    print(char," - is Undefined")