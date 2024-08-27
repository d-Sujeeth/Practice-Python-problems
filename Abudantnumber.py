n=37
prime=0
for i in range(2,n):
    if n%i==0:
        prime+=i
print(prime)
if prime>n:
    print("is a Abudant Number")
else:
    print("Not Abudant Number")