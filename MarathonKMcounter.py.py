n=int(input("Enter The KM: "))
count=0
a=[]
for i in range(0,n+1,2):
    a.append(i)
for j in a:
    count+=j
print(count)
