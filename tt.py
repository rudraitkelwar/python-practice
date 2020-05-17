import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    
    print("size of array")
    n = int(input())
    ar=[]
    s=1

    #while s<=n:
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


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
