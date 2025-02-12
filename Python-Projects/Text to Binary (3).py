#20210616

def text_to_binary(text):
    total_binary = ''

    for i in range(len(text)):
        binary = ''
        string_ord = ord(text[i:i+1])

        while string_ord > 0:
            x = string_ord % 2
            string_ord = string_ord // 2
            binary = str(x) + str(binary)
        total_binary += binary + ''

    print(total_binary)

text_to_binary(input("enter text"))
