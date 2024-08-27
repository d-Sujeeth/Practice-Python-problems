n=[4,1,5]
def first(i):
    if i==1:
        return 1
    else:
        return i*first(i-1)
a=0
for i in n:
    a+=first(i)
    print(a)