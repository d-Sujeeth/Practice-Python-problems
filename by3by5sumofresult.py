n1=int(input("Enter 1st Number: "))
n2=int(input("Enter 2nd number: "))
count=0
for i in range(n1,n2+1):
    if i%3==0 and i%5==0:
        count+=i
    else:
        count+=0
print(count)
