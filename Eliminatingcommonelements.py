n=input("Enter string 1: ")
b=input("Enter string 2: ")
for i in n:
    if i not in b:
        print(i,end="")