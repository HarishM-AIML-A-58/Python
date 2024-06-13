#Done by M Harish AIML-A 231501058
widgets = int(input())
gizmos = int(input())
widget_weight = widgets * 75
gizmo_weight = gizmos * 112
total_weight = widget_weight + gizmo_weight
print("The total weight of all these widgets and gizmos is {} grams.".format(total_weight))


number = int(input())
if number % 2 == 0 and number != 0 and number <= 100:
    print("True")
else:
    print("False")


N = int(input())
P1 = int(input())
P2 = int(input())
P3 = int(input())
P4 = int(input())
for packet in [P1, P2, P3, P4]:
    if packet % N == 0:
        print("True", end=" ")
    else:
        print("False", end=" ")

num = int(input())
count = 0
while num:
    count += num & 1
    num >>= 1

print(count)

principal = float(input())
interest_rate = 0.04
balance_year1 = principal * (1 + interest_rate)
balance_year2 = balance_year1 * (1 + interest_rate)
balance_year3 = balance_year2 * (1 + interest_rate)
print("Balance as of end of Year 1: ${:.2f}.".format(balance_year1))
print("Balance as of end of Year 2: ${:.2f}.".format(balance_year2))
print("Balance as of end of Year 3: ${:.2f}.".format(balance_year3))

age = int(input())
weight = int(input())
is_eligible = (age >= 18) * (weight > 40)
print(bool(is_eligible))


x = int(input())
if x == 0:
    print(chr(ord('C')))
else:
    print(chr(ord('C') + 1))

weapons = int(input())
soldiers = int(input())
if weapons % 3 == 0 and soldiers % 2 == 0:
    print("True")
else:
    print("False")


cost_of_meal = float(input())
tax_rate = 0.05
tip_rate = 0.18
tax_amount = cost_of_meal * tax_rate
tip_amount = (cost_of_meal * tip_rate)
total_cost = cost_of_meal + tax_amount + tip_amount
print("The tax is {:.2f} and the tip is {:.2f}, making the total {:.2f}".format(tax_amount, tip_amount, total_cost))



number = int(input())
last_digit = abs(number) % 10
print(last_digit)
#Done by M Harish AIML-A 231501058