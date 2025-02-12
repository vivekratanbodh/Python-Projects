n = int(input("Enter Three Digits Value"))
a = n%10
x = n//10
y = x%10
b = a%10
c = n//100

pel = a*100 + y*10 + c
if(n==pel):
    print(pel, "is a Pelendrom Number")
else:
    print(pel, "is not a Pelendrom Number")