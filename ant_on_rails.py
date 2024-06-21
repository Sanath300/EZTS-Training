def ant_on_rails(l):
    count=0
    m=0
    for i in l:
        m+=i
        if m==0:
            count+=1
        else:
            continue
    print(count)
l=[1]
ant_on_rails(l)
