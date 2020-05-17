k=0
#scores=[100,100,50,40,40,20,10]
#alice=[5,25,50,120]
scores=[100,90,90,80,75,60]
alice=[50,65,77,90,102]


scores.append(k)
res=[]
print(scores)
print(alice)
for i in range(len(alice)):
    if alice[i]>scores[0]:
            print(alice[i],"inserted in scores before",scores[0])
            print("giving rank 1 to",alice[i])
            res.append(1)
            scores.insert()
                
    else:
        if scores[0]!=scores[1]:      
            for j in range(0,len(scores)):
                print("checking",alice[i],scores[j])
                #if alice[i]>=scores[j]:
                
                if alice[i]>scores[j]:
                    
                    print(alice[i],"inserted in scores before",scores[j])
                    scores.insert(j,alice[i])
                    print("giving rank ",str(j-1),"to",alice[i])
                    res.append(j)
                        
                    break
                        
                        
                elif alice[i]==scores[j]:
                    
                    print(alice[i],"inserted in scores before",scores[j])
                    scores.insert(j,alice[i])
                    #print(str(j))
                    print("giving rank ",str(j),"to",alice[i])
                    res.append(j+1)
                        
                    break
        elif scores[0]==scores[1]:
            for j in range(1,len(scores)):
                print("checking",alice[i],scores[j])
                #if alice[i]>=scores[j]:
                
                if alice[i]>scores[j]:
                    
                    print(alice[i],"inserted in scores before",scores[j])
                    scores.insert(j,alice[i])
                    print("giving rank ",str(j-1),"to",alice[i])
                    res.append(j-1)
                        
                    break
                        
                        
                elif alice[i]==scores[j]:
                    
                    print(alice[i],"inserted in scores before",scores[j])
                    scores.insert(j,alice[i])
                    #print(str(j))
                    print("giving rank ",str(j),"to",alice[i])
                    res.append(j)
                        
                    break
        
print(res)
                