def hcf(x,y):
    if n1>n2:
        small = y
    else:
        small = x
    
    for i in range (1, small+1):
        if ((x%i == 0) and (y%i == 0)):
            hcf=i
    return hcf

n1 = int(input("Enter Value : "))
n2 = int(input("Enter Value : "))
print("HCF", n1, "and", n2, "is", hcf(n1,n2))