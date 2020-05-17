n=5
total=0
t=0
total=0
for c in range(n):
    if c==0:
        print("applying for 1 ")
        t=2
        total=2
        print("total after 1 is ",total)        
    else:
        print("applying for ",c) 
        total=int(total+(int((3*t)/2)))
        t=int((t*3)/2)
        print("total after ",c,"is",total)
        


print(t)
print(total)



    

