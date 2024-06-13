s1 = input()
s2 = input()

words1 = s1.split()
words2 = s2.split()

count = {}
for word in words1 + words2:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

uncommon_words = [word for word in count if count[word] == 1]

print(uncommon_words)


n=int(input())
l1=[]
l2=[]
l3=[]
d=dict()
for i in range(n):
   l1=input().split(" ")
   l2.append(l1[0])
   l1.pop(0)
   l3.append(l1)
for j in range(len(l3)):
    sum=0
    for k in l3[j]:
        sum+=int(k)
    l3[j]=sum
for i in range(len(l2)):
    d[l2[i]]=l3[i]
dn=dict(sorted(d.items(),key=lambda items:items[1]))
for key,value in dn.items():
    print(f"{key} {value}")
 


PROGRAM
n=int(input())
l1=[]
d=dict()
for i in range(n):
    l1.append(input())
for j in l1:
    d[j]=l1.count(j)
n1=max(d)
m=d[n1]
d.pop(n1)
n2=max(d)
if(m== d[n2]):
    if(len(n1)<len(n2)):
        print(n1)
    else:
        print(n2)
else:
    print(n1)
    




n=int(input())
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
for i in range(n):
    student_data=input()
    student_input_parts=student_data.split()
    name=student_input_parts[0]
    marks=[int(mark) for mark in student_input_parts[1:]]
    average=(marks[0]+marks[1]+marks[2])/3
    list1.append(name)
    list2.append(marks[0])
    list3.append(marks[1])
    list4.append(marks[2])
    list5.append(average)
l1=[]

for i in range(n):
    if list5[i]==max(list5):
            l1.append(list1[i])
for i in l1:
    print(i,end=' ')
print()
l2=[]
for i in range(n):
    if list3[i]==max(list3):
        l2.append(list1[i])
for i in l2:
    print(i,end=' ')
print()
l3=[]
for i in range(n):
    if list4[i]==min(list4):
        l3.append(list1[i])
l3.reverse()
for i in l3:
    print(i,end=' ')
print()
l4=[]
for i in range(n):
    if list5[i]==min(list5):
            l4.append(list1[i])
for i in l4:
    print(i,end=' ')
 


s=input()
l1=list(s)
d=dict([(1,['A','E','I','L','N','O','R','S','T','U']),(2,['D','G']),(3,['B','C','M','P']),(4,['F','H','V','W','Y']),(5,['K']),(8,['J','X']),(10,['Q','Z'])])
sum=0
for j in l1:
    for key,values in d.items():
        if j in values:
            sum+=key
print(f"{s} is worth {sum} points.")
