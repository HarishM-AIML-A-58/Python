#Done by M Harish AIML-A 231501058
x = str(input())

c1, c2, c3 = 0, 0, 0

for i in x:
    if i.isalpha():
        c1 += 1
    elif i.isdigit():
        c2 += 1
    else:
        c3 += 1

print(c1)
print(c2)
print(c3)



s=input()
l1=[]
l2=[]
s2=""
for i in range(0,len(s)):
    if((ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122)):
        l1.append(s[i])
    else:
        s2=s2+s[i]
        continue
    if s2!="":
        l2.append(s2)
    s2=""
i=-1
while(s[i]==ord(s[i])>=48 and ord(s[i])<=57):
    s2=s2+s[i]
    i-=1
    continue
l2.append(s2)
for i in range(0,len(l2)):
    l2[i]=int(l2[i])
for i in range(0,len(l1)):
    print(l1[i]*l2[i],end="")



s1 = input().strip()
s2 = input().strip()
n = int(input())
common_chars = ''
for char in s1:
    if char in s2 and char not in common_chars:
        common_chars += char
        if len(common_chars) == n:
            break
print(common_chars)


str1=str(input())
str2=str(input())
l1=list(str1)
l2=list(str2)
for i in range(0,len(l2)):
    for j in range(0,len(l1)):
        if l2[i] in l1:
            l1.remove(l2[i])
str3=""
for i in range(0,len(l1)):
    str3=str3+l1[i]
print(str3)


x = input()

words = x.split()
non_palindrome_words = []

for word in words:
    word_lower = word.lower()
    if word_lower != word_lower[::-1]:
        non_palindrome_words.append(word_lower)

for word in non_palindrome_words:
    print(word, end=' ')


a=input()
l=a.split()
#print(l)
if(len(l)<2):
    print("LESS")
else:
    a=l[1]
    print(a.upper())


s = input().strip()
left, right = 0, len(s) - 1
s_list = list(s)

while left < right:
    if not s_list[left].isalpha():
        left += 1
    elif not s_list[right].isalpha():
        right -= 1
    else:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

result = ''.join(s_list)
print(result)


x = input()
y = input()
if x in y:
    print("True")
else:
    print("False")


b = input()
s1 =[]
c = 0
while b != " ":
    s1.append(b)
    b = input()
my_set = list(set(s1))
for i in s1:
    for j in range(len(my_set)):
        if i == my_set[j]:
            print(i)
            my_set[j] = "0000"


b=0
c=0
a=input()
if '@' in a:
    b=a.index("@")
if "." in a:
    c=a.index(".")

print(a[c+1:])
print(a[b+1:c])
print(a[:b])
#Done by M Harish AIML-A 231501058