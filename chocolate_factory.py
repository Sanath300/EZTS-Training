#METHOD1
L=[4,0,5,0,1,9,0,0]
j=0
for i in range(len(L)):
    if L[i]!=0:
        L[j]=L[i]
        j=j+1

while j<len(L):
    L[j]=0
    j=j+1
 
print(L)

#METHOD2

L=[0,4,0,0,0,5,0,1,9,0,0]
for i in L:
    if i==0:
        L.remove(i)
        L.append(i)
print(L)