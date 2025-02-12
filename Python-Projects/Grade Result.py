sub1 = int(input("Enter Subject 1 Marks : "))
sub2 = int(input("Enter Subject 2 Marks : "))
sub3 = int(input("Enter Subject 3 Marks : "))

if((sub1+sub2+sub3) >= 30):
    print("Pass")
elif((sub1+sub2+sub3) < 30):
    print("Fail")
else:
    print("Over Grade")