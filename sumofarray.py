
print("size of array")
n = int(input())
ar=[]
s=1

while s<=n:
    for c in range(n):
        print("add element")
        f=int(input())
        ar.append(f)
        s=s+1
m=0
for i in range(len(ar)):
        m=m+ar[i]
print("sum is")
print(m)

