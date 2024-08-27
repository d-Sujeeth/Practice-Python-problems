def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a=int(input("A: "))
b=int(input("B: "))
print(gcd(a,b))