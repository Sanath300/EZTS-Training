l=[3,4,5,3,2,4,4,2,6,6]
m={}
for i in range(len(l)):
    count=0
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            break
        else:
            count+=1
    m[l[j]]=count
m = {k: v for k, v in m.items() if v != 0}
print(min(m,key=m.get))