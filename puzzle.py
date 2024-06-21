# Problem Statement:
# In the enchanted land of Numeria, Alice is on a quest to find the legendary
# Prime Key to unlock the ancient Vault of Secrets. The vault's guardian, an
# ancient sphinx, presents a multi-step puzzle that Alice must solve to obtain the
# Prime Key.
# The puzzle consists of multiple levels, each requiring Alice to solve a different
# challenge involving prime numbers. To progress through each level, Alice must
# perform the following tasks:
# Level 1: Find the smallest prime number larger than a given integer N.
# Level 2: Calculate the sum of all prime numbers between N and the smallest
# prime number larger than N.
# Level 3: Determine if the product of the smallest prime number larger than N
# and the next immediate prime number is also a prime.
# To complete the puzzle and retrieve the Prime Key, Alice must solve these
# challenges in sequence for a given integer N.
# Your task is to write a function that takes an integer N and returns a tuple
# containing the following:
# - The smallest prime number larger than N (Level 1 result).
# - The sum of all prime numbers between N and the smallest prime number
# larger than N (Level 2 result).
# - A boolean indicating whether the product of the smallest prime number
# larger than N and the next immediate prime number is prime (Level 3 result).
# Help Alice navigate through the levels, solve the puzzle, and obtain the Prime
# Key to unlock the Vault of Secrets.
def puzzle(n):

    f=0
    if n<1:
        return -1
    elif f==1:
        return 1
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                f=1
    if f<2:
        return 1
    else:
        return -1
result=[]
n=int(input("enter: "))
flag=0
k=n+1
while flag<1:
    flag=puzzle(k)
    if flag==1:
        result.append(k)    
    else:
        k+=1
b=0
for i in range(n+1,k):
    b+=i
result.append(b)
p1=k
g=p1+1
f=0
while f<1:
    f=puzzle(g)
    if f==1:
        pro=g*p1
        h=puzzle(pro)
        if h==1:
            result.append(True)
        else:
            result.append(False)     
    else:
        g+=1
t=tuple(result)
print(t)