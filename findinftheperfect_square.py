a=[25,36,12,81]
b=max(a)
count=0
for i in range(b+1):
    for j in a:
        if i*i==j:
            count+=1
print(count)