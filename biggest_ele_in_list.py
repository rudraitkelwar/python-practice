mylist=[11,44,22,4,56,89,55,56,88,97,35,78,108,19]

def biggest(list):
    i=0
    biggest=0
    while i<=len(list):
        for c in range(len(list)):
            i=i+1
            if list[c]>biggest:
                biggest=list[c]
    return biggest


print(biggest(mylist))