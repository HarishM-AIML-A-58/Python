a=int(input())
for i in range(1,a+1):
      if (a%i==0):
          print(i,end=’ ‘)

num=int(input())
count=0
last=len(str(num))
for i in range(1,last):
      temp=num%10
num=num//10
if (str(temp)not in str(num)):
	count+=1
if(len(str(num))==1 and count==last-1):
    print(count+1)
else:
    print(count)


a=int(input())
count=0
for i in range(2,a):
      if (a%i==0):
          count+=1
if(count==0):
      print(“2”)
else:
      print(“1”)


from math import sqrt
num=int(input())
while True:
a=int(sqrt(num))
	if(num==pow(a,2)):
	   print(num)
	   break
	else:
	   num+=1



a=int(input())
b=0
c=1
d=0
for i in range(3,a+1):
      d=c+b
      b=c
c=d
print(d)



num=int(input())
last=len(str(num))
temp=num
Sum=0
for i in range(0,last):
       n=temp%10
       temp=temp//10
       sum=sum+(pow(n,last-i))
if (sum==num):
    print(“Yes”)
else:
     print(“No”)


num=int(input())
sum1=0
for i in range(1,num+1):
      st=’1’*i
      sum1=sum1+int(st)
print(sum1)


num=int(input())
count=0
last=len(str(num))
for i in range(1,last):
       n=num%10
num=num//10
if (str(n)not in str(num)):
	count+=1
print(count+1)



a=int(input())
count=0
for i in range(1,10):
      for j in range(1,10):
            if (i*j==a):
                print(“Yes”)
                count+=1
                break
      if(count>0):
          break
if(count==0):
   print(“No”)

from math import sqrt
num=int(input())
fin=num+1
sq=int(sqrt(fin))
if (fin==pow(sq,2)):
    print(“Yes”)
else:
    print(“No”)
