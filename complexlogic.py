n=int(input("Divisor: "))
m=int(input("Range: "))
divi=0
notdivi=0
for i in range(m+1):
    if i%n==0:
        divi+=i
    else:
        notdivi+=i
print(notdivi-divi)