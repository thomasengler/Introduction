"""
▪ Take the program from Exercise 6 and add some more
statements for printing out a positive encouragement
 Input 1 > Input 2 and Input 3 > Input 4
 Input 1 < Input 3 and Input 2 < Input 4
 Input 1 = Input 4 or Input 2 >= Input 3
 Input 1 <= Input 4 and Input2 = Input 3
"""
#sum of numbers
allno = int(4)
#input four numbers
no1 = float(input(f"First number out of {allno}\n"))
no2 = float(input(f"Second number out of {allno}\n"))
no3 = float(input(f"third number out of {allno}\n"))
no4 = float(input(f"Fourth number out of {allno}\n"))

if no1==no2 and no3 == no4:
    print("Task accomplished")
elif no1==no3 and no2 == no4:
    print("Task accomplished")
elif no1==no4 or no2 == no3:
    print("Task accomplished")
elif no1 > no2 and no3 > no4:
    print("Task accomplished")
elif no1 < no3 and no2 < no4:
    print("Task accomplished")
elif no1 == no4 or no2 >= no3:
    print("Task accomplished")
elif no1 <= no4 and no2 == no3:
    print("Task accomplished")
else:
    print("Conditions are not fullfilled")

#shorter
print()
if (no1==no2 and no3 == no4) or (no1==no3 and no2 == no4) or (no1==no4 or no2 == no3) or (no1 > no2 and no3 > no4) or (no1 < no3 and no2 < no4) or (no1 == no4 or no2 >= no3) or (no1 <= no4 and no2 == no3):
    print("Task accomplished")
else:
    print("Conditions are not fullfilled")
