#Done by M Harish AIML-A 231501058
a = int(input())
b = list(input().split(" "))
b.sort()
for i in b:
    print(i,end=" ")


num = 0
a = int(input())
b = input().split(" ") 
c = []

for i in range(len(b)):
    c.append(int(b[i]))

for j in range(len(c)):
    for i in range(len(c)-1):
        if c[i] > c[i+1]:
            c[i], c[i+1] = c[i+1], c[i]
            num += 1

print(f"List is sorted in {num} swaps.\nFirst Element: {c[0]}\nLast Element: {c[-1]}")



n = int(input())
A = list(map(int, input().split()))
if n == 1:
    print(A[0])
else:
    if A[0] >= A[1]:
        print(A[0], end=" ")
    for i in range(1, n - 1):
        if A[i] >= A[i - 1] and A[i] >= A[i + 1]:
            print(A[i], end=" ")
    if A[n - 1] >= A[n - 2]:
        print(A[n - 1])



def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

arr = list(map(int, input().split(',')))
x = int(input())
arr.sort()
result = binary_search(arr, x)
print(result)


numbers = input().split()
numbers = [int(num) for num in numbers]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
   
 else:
        frequency[num] = 1
sorted_frequency = sorted(frequency.items())
for key, value in sorted_frequency:
    print(key, value)
#Done by M Harish AIML-A 231501058