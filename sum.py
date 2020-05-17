ar=[10,20,20,10,10,30,50,10,20]
n=9
count=0
a=[]
for c in range(100):
    a.append(0)
for i in range(n):
    a[ar[i]]=a[ar[i]]+1
for j in range(100):
    if a[j]!=0 and a[j]%2==0:
        count=count+(a[j]/2)
    elif a[j]!=0:
        m=a[j]-1
        count=count+(m/2)

print(a)
print(int(count))