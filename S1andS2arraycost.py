s1 = [1, 4, 5]
s2 = [1, 4, 5, 6, 9]
samevalue = 0
initlen=len(s1)
for i in s2:
    if i in s1:
        samevalue += 1
    else:
        s1.append(i)
        