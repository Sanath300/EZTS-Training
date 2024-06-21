def sort_twos(m1):
    count1,count2,count0=0,0,0
    for i in range(len(m1)):
        if m1[i]==0:
            count0+=1
        elif m1[i]==1:
            count1+=1
        else:
            count2+=1
    j=0
    while count0>0:
        m1[j]=0
        j+=1
        count0-=1

    while count1>0:
        m1[j]=1
        j+=1
        count1-=1
    while count2>0:
        m1[j]=2
        j+=1
        count2-=1
        
    print(m1)

m1=[2,1,0,1,1,2,0,0]
sort_twos(m1)