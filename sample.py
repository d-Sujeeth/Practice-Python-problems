number=int(input("Enter decimal: "))
strs=""
while number>0:
    strs=str(number%2) + strs
    number=number//2
print(strs)