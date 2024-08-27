strs=input()
a=input()
b=input()
el=[]
final=""
for l in strs:
    el.append(l)
for i in range(len(strs)-1):
    if el[i]==a:
        el[i]=b
    elif el[i]==b:
        el[i]=a
for o in el:
    final+=o
print(final)