import math
n = int(input())
print(n > 0 and math.log2(n).is_integer())


import math
diameter, tile_size = map(float, input().split())

radius = diameter / 2
area_pool = math.pi * (radius ** 2)
tile_size_m = tile_size / 100
area_tile = tile_size_m ** 2

tiles_needed = math.ceil(area_pool / area_tile)
print(f"{tiles_needed} tiles")



no_of_shoes=int(input())
size=input().split()
size=[int(x) for x in size]
customers=int(input())
total=0
for i in range(customers):
    new=input().split()
    new=[int(x) for x in new]
    if new[0] in size:
        size.remove(new[0])
        total+=new[-1]
print(total)
 



n=int(input())
l=input().split()
l=[int(x) for x in l]
k=int(input())
sum=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if abs(l[i]-l[j])==k :
            sum+=1
print(sum)


import math
n = int(input())
columns = input().split()
marks_index = columns.index("MARKS")

total_marks = 0
for _ in range(n):
    data = input().split()
    total_marks += int(data[marks_index])

average_marks = total_marks / n
print(f"{average_marks:.2f}")

 
