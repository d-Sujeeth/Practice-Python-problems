n=int(input())
l=[]
for i in range(n):
    lst=list(map(int,input().split()))
    l.append(lst)
for k in range(len(l)):
    for j in l[k]:
        print(j)
