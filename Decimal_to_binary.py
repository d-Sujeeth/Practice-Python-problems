n,b=15,''
while n>0:
    b=str(n%2)+b
    n=n//2
print(f"the Binary Value of N is {b}")