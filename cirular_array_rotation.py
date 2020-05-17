a=[1,2,3]
k=2
queries=[0,1,2]

n=len(a)
for s in range (len(queries)):
    m = queries[s]
    i = (m - k) % n
    #return (a[i])
    print(a[i])



