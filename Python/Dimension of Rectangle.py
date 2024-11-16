print("To find type 0\n")

l=int(input("Enter Length : "))
b=int(input("Enter Breadth : "))
a=int(input("Enter Area : "))

print("\n")

#Area
if(l==0):
    print("Length of Rectangle : ", a//b)
elif(b==0):
    print("Breadth of Rectangle : ", a//l)
else:
    print("Area of Rectangle : ", l*b)

print("\n")

#Perimeter

p=int(input("Enter Perimeter : "))

if(l==0):
    print("Length of Rectangle : ", (p//2)-b)
if(b==0):
    print("Breadth of Rectangle : ", (p//2)-l)
else:
    print("Perimeter of Rectangle : ", l+l+b+b)