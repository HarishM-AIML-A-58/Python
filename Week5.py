#Done by M Harish AIML-A 231501058
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
total_sum = sum(arr)
left_sum = 0
for i in range(n):
    if left_sum == total_sum - arr[i] - left_sum:
        print(i)
        break
    left_sum += arr[i]


t=int(input())
for q in range(t):
    n1=int(input())
    x=0
    l1=[]
    for j in range(n1):
        e=int(input())
        l1.append(e)
    k=int(input())
    for i in range(n1):
        for l in range(n1):
            if(l1[i]-l1[l]==k and i!=l):
                x=1
                break
    print(x)

n=int(input())
l=[]
freq={}
for i in range(n):
    a=int(input())
    l.append(a)

for item in l:
    if (item in freq):
        freq[item]+=1
    else:
        freq[item]=1

for key, value in freq.items():
    print("{0} occurs {1} times".format(key, value))




list1=[]
n=int(input())
for i in range(n):
    a=int(input())
    list1.append(a)
    a1=set(list1)
list2=list(a1)
for i in range(len(list2)):
    print(list2[i],end=' ')


lst=[]
for i in range(0,10):
    l1=int(input())
    lst.append(l1)

l2=int(input())
lst.append(l2)
print("ITEM to be inserted:{0}".format(lst[-1]))
print("After insertion array is:")
lst.sort()
for i in lst:
    print(i)


a=int(input())
b=int(input())
l=[]
for i in range(1,21):
    if a%i==0:
        l.append(i)
        
if b<=len(l):
    print(l[b-1])
else:
    print("0")
        

m = int(input())
n = int(input())
list1 = []
for _ in range(m):
    row = [int(input()) for _ in range(n)]
    list1.append(row)
list2 = []
for _ in range(m):
    row = [int(input()) for _ in range(n)]
    list2.append(row)
zipped_list = [list(a + b) for a, b in zip(list1, list2)]
print(zipped_list)


lst=[]
n1=int(input())
for i in range(0,n1):
    l1=int(input())
    lst.append(l1)
n2=int(input())
for j in range(0,n2):
    l2=int(input())
    lst.append(l2)

d=set(lst)
e=list(d)
e.sort()
for i in e:
    print(i,end=' ')


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
element_to_search = int(input())
locations = []
count = 0
for i in range(n):
    if arr[i] == element_to_search:
        locations.append(i + 1)
        count += 1
if count > 0:
    for loc in locations:
        print(f"{element_to_search} is present at location {loc}.")
    print(f"{element_to_search} is present {count} times in the array.")
else:
    print(f"{element_to_search} is not present in the array.")


import copy
n1=int(input())
l1=[]
x=0
for i in range(n1):
    e=int(input())
    l1.append(e)
if(l1==sorted(l1) or l1==sorted(l1,reverse=True)):
        x=1
else:
    for j in range(0,n1):
        l2=copy.copy(l1)
        del l2[j]
        if(l2==sorted(l2) or l2==sorted(l2,reverse=True)):
            x=1
            break
print(bool(x))
#Done by M Harish AIML-A 231501058