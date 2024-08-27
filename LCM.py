n=int(input("Enter N : "))
m=int(input("Enter M : "))
if n>m:
    maxx=n
else:
    maxx=m
lcm=0
for i in range(maxx,n*m+1):
    if i%n==0 and i%m==0:
        lcm+=i
        break
print(lcm)