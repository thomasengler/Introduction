"""
▪ Rework your program from Exercise 07 with the use of
nested if statements instead of the logical operators:
 and
 or
"""
#sum of numbers
allno = int(4)
#input four numbers
no1 = float(input(f"First number out of {allno}\n"))
no2 = float(input(f"Second number out of {allno}\n"))
no3 = float(input(f"third number out of {allno}\n"))
no4 = float(input(f"Fourth number out of {allno}\n"))

if no1 == no2:
    if no3 == no4:
        print("Task accomplished")

if no1 == no3:
    print("Task accomplished")
    if no2 == no4:
        print("Task accomplished")

if no2 == no3:
    if no1 <= no4:
        print("Task accomplished")
    elif no1 == no4:
        print("Task accomplished")

if no2 == no3:
    print("Task accomplished")

if no1 == no4:
    print("Task accomplished")

if no2 >= no3:
    print("Task accomplished")

if no1 > no2:
    print("Task accomplished")
    if no3 > no4:
        print("Task accomplished")

if no1 < no3:
    print("Task accomplished")
    if no2 < no4:
        print("Task accomplished")

else:
    print("Conditions are not fullfilled")
