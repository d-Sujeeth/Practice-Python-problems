a=int(input("Enter no: "))
b=int(input("Enter no: "))
c=int(input("Enter no: "))
if a>b and a>c:
    print("the output is= ",a)
elif b>a and b>c:
    print("the output is= ",b)
elif c>a and c>b:
    print("the output is= ",c)
else:
    print("All Numbers are Equal in value")