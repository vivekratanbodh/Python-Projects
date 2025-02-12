n = int(input("Enter Three Digits Value : "))

a = n % 10
x = n // 10
y = x % 10
b = a % 10
c = n // 100
arm = a**3 + y**3 + c**3

if(n==arm):
    print(n, "is an Armstrong Number")
else:
    print(n, "is not a Armstrong Number")