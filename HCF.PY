n=int(input("Number one: "))
m=int(input("Number Two: "))
fact_n=[]
for i in range(1,n+1):
    if n%i==0 and m%i==0:
        fact_n.append(i)
a=max(fact_n)
print(a)
