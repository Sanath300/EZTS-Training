def armstrong():
    n=int(input("Enter the number: "))
    sum,count=0,0
    m=str(n)
    temp,atemp=n,n
    while temp>0:
        count+=1
        temp=temp//10
    print(count)
    while n>0:
        digit=n%10
        sum+=digit**count
        n=n//10
    if sum==atemp:
        print("Yep")
        return
    print("Nope")
armstrong()