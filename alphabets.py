n=3
if n==0:
    #return 1
    print(1)
else:
    h=1
    for i in range(0,n):
        if i%2==0:
            h=h*2
            print("i=",i)
            print("height is doubled  ",h)
        else:
            h=h+1
            print("i=",i)
            print("height is increased by 1",h)
    #return h 
    print(h)   
