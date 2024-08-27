number,b = int(input("Enter the number: ")),""
p,u = 0,""
while number > 0:
    b = str(number % 2) + b
    number = number // 2
print("Binary form of input:",b)
a = ""
for j in b:
    if j == "1":
        u+="2"
    elif j == "0":
        u+="1"
print("Replaced value of Binary Number:",u)
for i in u:
    p += int(i)
if p%2!=0:
    print("Magical Number")
else:
    print("Is Not magical Number")