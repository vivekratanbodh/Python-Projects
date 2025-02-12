n=int(input("Enter two Digit Number:\t"))
rev=0
while(n>0):
    dig = n % 10
    rev = rev*10 + dig
    n = n//10
print("Reversed Number:\t", rev)