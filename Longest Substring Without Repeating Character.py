n=['p',"w","k","e","w"]
s=""
a=[]
for i in n:
    print(i)
    if i in a:
        break
    else:
        a.append(i)
for j in a:
    s+=j
print(f"The substring is : {s}")
print(f"length is : {len(s)}")