def count_commas():
    num = int(input("Enter the number up to which the commas should be counted: "))
    if num < 1000:
        print(0)
    elif num < 1000000:
        print((num - 1000) + 1)
    else:
        commas_one = 999000
        commas_two = (num - 999999) * 2 
        total_commas = commas_one + commas_two
        print(total_commas)

count_commas()
def separators(n):
    count=0
    for i in range(1,n+1):
        if i>999 and i<99999:
            count+=1
        elif i>99999 and i<999999999:
            count+=2
    print(count)

n=int(input("Enter number: "))
separators(n)