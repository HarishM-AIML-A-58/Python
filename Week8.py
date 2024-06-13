#Done by M Harish AIML-A 231501058
str=input()
str=[x for x in str]
str=set(str)
c=0
if '0' in str and '1' in str:
    c+=2
if(c==len(str)):
    print("Yes")
else:
    print("No")

s=input()
l1=s.split(',')
n=int(input())
l2=[]
for i in range(len(l1)):
    j=i+1
    for j in range(len(l1)):
        if(int(l1[i])+int(l1[j])==n):
            l2.append(list[l1[i],l1[j]])
s=set(l2)

print(len(s)//2)


s = input()
sequence_length = 10
seen = {}
result = []
for i in range(len(s) - sequence_length + 1):
    sequence = s[i:i + sequence_length]
    if sequence in seen:
        seen[sequence] += 1
    else:
        seen[sequence] = 1

for sequence, count in seen.items():
    if count > 1:
        result.append(sequence)
for i in result:
    print(i)


st=input()
nums=st.split()
for i in nums:
    if nums.count(i)==2:
        b=nums.index(i)
print(nums[b])



sizes = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
set1 = set(arr1)
set2 = set(arr2)
unique1 = set1 - set2
unique2 = set2 - set1

unique_elements = list(unique1) + list(unique2)

if unique_elements:
    print(" ".join(map(str, unique_elements)))
    print(len(unique_elements))
else:
    print("NO SUCH ELEMENTS")


s1=str(input())
s2=str(input())
l1=(s1.lower()).split(' ')
l2=list(s2)
for i in l2:
    for word in l1:
        if i in list(word):
            l1.remove(word)
print(len(l1))


n=int(input())
l=[]
for j in range(n):
    l.append(str(input()))
row1 = set("qwertyuiop")
row2 = set("asdfghjkl")
row3 = set("zxcvbnm")
result = []
for word in l:
    lower_word = set(word.lower())
    if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
        result.append(word)
if(len(result)!=0):
    for i in range(len(result)):
        print(result[i])
else:
    print("No words")
#Done by M Harish AIML-A 231501058