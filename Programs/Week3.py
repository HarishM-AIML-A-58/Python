#Done by M Harish AIML-A 231501058
m1=int(input())
m2=int(input())
m3=int(input())
if (m1>=65 and m2>=55 and m3>=50) or ((m1+m2+m3)>=180):
    print("The candidate is eligible")
else:
    print("The candidate is not eligible")


m1=int(input())
m2=int(input())
m3=int(input())
if m1==m2 and m1==m3:
    print("That's a equilateral triangle")
elif (m1==m2 and m1!=m3) or (m2==m3 and m3!=m1) or (m1==m3 and m3!=m2):
    print("That's a isosceles triangle")
else:
    print("That's a scalene triangle")


unit = float(input())
if unit <= 199:
    charge = unit * 1.20
elif unit < 400:
    charge = unit * 1.50
elif unit < 600:
    charge = unit * 1.80
else:
    charge = unit * 2.00
if charge > 400:
    surcharge = charge * 0.15
    total_amount = charge + surcharge
else:
    total_amount = charge
if total_amount < 100:
    total_amount = 100
print("{:.2f}".format(total_amount))


problems_given = int(input())
problems_solved = int(input())
if problems_solved >= problems_given / 2:
    print("IN")
else:
    print("OUT")


a=input()
if a in ('a','e','i','o','u'):
    print("It's a vowel.")
elif a=='y':
    print("Sometimes it's a vowel... Sometimes it's a consonant.")
else:
    print("It's a consonant.")


year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


a=input()
if a=='January':
    print(a,"has 31 days in it.")
elif a=="February":
    print(a,"has 28 or 29 days in it.")
elif a=="March":
    print(a,"has 31 days in it.")
elif a=="April":
    print(a,"has 30 days in it.")
elif a=="May":
    print(a,"has 31 days in it.")
elif a=="June":
    print(a,"has 30 days in it.")
elif a=="July":
    print(a,"has 31 days in it.")
elif a=="August":
    print(a,"has 31 days in it.")
elif a=="September":
    print(a,"has 30 days in it.")
elif a=="October":
    print(a,"has 31 days in it.")
elif a=="November":
    print(a,"has 30 days in it.")
elif a=="December":
    print(a,"has 31 days in it.")


a = int(input())
b = int(input())
c = int(input())
if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("yes")
else:
    print("no")


if len(num) == 1:
    print(-1)
else:
    print(num[-2])


year = int(input())
animal = ""
if year >= 2000:
    offset = (year - 2000) % 12
    if offset == 0:
        animal = "Dragon"
    elif offset == 1:
        animal = "Snake"
    elif offset == 2:
        animal = "Horse"
    elif offset == 3:
        animal = "Sheep"
    elif offset == 4:
        animal = "Monkey"
    elif offset == 5:
        animal = "Rooster"
    elif offset == 6:
        animal = "Dog"
    elif offset == 7:
        animal = "Pig"
    elif offset == 8:
        animal = "Rat"
    elif offset == 9:
        animal = "Ox"
    elif offset == 10:
        animal = "Tiger"
    elif offset == 11:
        animal = "Hare"
print(year, "is the year of the", animal + ".")
#Done by M Harish AIML-A 231501058