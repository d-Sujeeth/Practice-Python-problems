n=int(input("Enter number: "))
sum=0
for i in range(2,n+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        sum+=i
print(sum)