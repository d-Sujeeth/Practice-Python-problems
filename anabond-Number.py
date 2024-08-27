n=input("Enter Number : ")
pa=n[::-1]
s=int(n)**2
p=int(pa)**2
l=str(p)
if str(int(n)**2)==l[::-1]:
    print(f"{n} is a Anabond Number")
else:
    print("No")