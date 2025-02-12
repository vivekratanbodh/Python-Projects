f = int(input("Enter Value"))
print("The Factors of", f)

for i in range (1, f+1):
    if (f % i == 0):
        print(i)