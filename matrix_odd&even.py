n1=list(map(int,input().split()))
even=""
odd=""
for i in range(0,len(n1),2):
    even+=str(n1[i])
for j in range(1,len(n1),2):
    odd+=str(n1[j])
sortedeven=sorted(even)
sortedodd=sorted(odd)
print(sortedeven,sortedodd)
print(int(sortedeven[len(sortedeven)-2])+int(sortedodd[len(sortedodd)-2]))


