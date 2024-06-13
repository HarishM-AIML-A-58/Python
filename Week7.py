def abundant(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i 
    if sum>n:
        return ("Yes")
    else:
        return ("No")


def automorphic(n):
    if(n==((n**2)%10)):
        return("Automorphic")
    else:
        return("Not Automorphic")


def productDigits(n):
    s=str(n)
    sum=0
    for j in range(1,len(s)):
        if(j%2!=0):
            sum+=int(s[j])
    sum1=0
    while(n>0):
        n1=n%10
        n=n//10
        sum1+=n1
    if(sum1%sum==0):
        return False
    else:
        return True


def christmasDiscount(n):
    count=0
    sum=0
    while(n>0):
        count=0
        n1=n%10
        n=n//10
        for i in range(2,n1):
            if(n1%i==0):
                count=1
        if(count==0):
            sum+=n1
    return sum


def coinChange(n):
    coins = [4, 3, 2, 1]
    count = 0
    for coin in coins:
        count += n // coin
        n %= coin
    return count


def differenceSum(n):
    st=str(n)
    evensum=0
    oddsum=0
    for i in st:
        if int(i)%2==0:
            evensum+=int(i)
        else:
            oddsum+=int(i)
        return abs(evensum-oddsum)


def checkUgly(n):
    while n % 2 == 0:
        n //= 2

    while n % 3 == 0:
        n //= 3

    while n % 5 == 0:
        n //= 5

    return "ugly" if n == 1 else "not ugly"
