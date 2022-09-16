"""
▪ Write a program that takes at least 6 different numbers as
input from the user
▪ Then ask the user which of the four standard mathematical
operations the program should run over these numbers

Use Print commands to show the user what options he has
▪ Create an if-statement that checks what option the user
chose (use if elif else)

don’t forget to include a security check
▪ Run your mathematical operations inside this statement
▪ Print out the results by using f-strings or commas
"""
#sum of numbers
allno = int(6)

#input six different numbers
no1 = float(input(f"First number out of {allno}\n"))
no2 = float(input(f"Second number out of {allno}\n"))
no3 = float(input(f"Third number out of {allno}\n"))
no4 = float(input(f"Fourth number out of {allno}\n"))
no5 = float(input(f"Fifth number out of {allno}\n"))
no6 = float(input(f"Sixth number out of {allno}\n"))


#user question: Which four standard mathematical to use
operator=input("What do you want to do?\nPossible options: +,-,*,/\n")


#older version
if operator == "+":
    res = no1+no2+no3+no4+no5+no6
    print(f"________________________________________________________________________\n{no1} {operator} {no2} {operator} {no3} {operator} {no4} {operator} {no5} {operator} {no6} {operator} = {res}")
    print("=========================================================================")
elif operator == "-":
    res = no1-no2-no3-no4-no5-no6
    print(f"________________________________________________________________________\n{no1} {operator} {no2} {operator} {no3} {operator} {no4} {operator} {no5} {operator} {no6} {operator} = {res}")
    print("=========================================================================")
elif operator == "*":
    res = no1*no2*no3*no4*no5*no6
    print(f"________________________________________________________________________\n{no1} {operator} {no2} {operator} {no3} {operator} {no4} {operator} {no5} {operator} {no6} {operator} = {res}")
    print("=========================================================================")
elif operator == "/":
    res = no1/no2/no3/no4/no5/no6
    print(f"________________________________________________________________________\n{no1} {operator} {no2} {operator} {no3} {operator} {no4} {operator} {no5} {operator} {no6} {operator} = {res}")
    print("=========================================================================")
else:
    print ("Error, choose only from the aviable options!\n +,-,*,/")

""""

#shorter
res = 0
print1 = print(f"________________________________________________________________________\n{no1} {operator} {no2} {operator} {no3} {operator} {no4} {operator} {no5} {operator} {no6} {operator} = {res}\n=========================================================================")

if operator == "+":
    res == no1+no2+no3+no4+no5+no6
    print1
elif operator == "-":
    res == no1-no2-no3-no4-no5-no6
    print1
elif operator == "*":
    res == no1*no2*no3*no4*no5*no6
    print1
elif operator == "/":
    res == no1/no2/no3/no4/no5/no6
    print1
else:
    print ("Error, choose only from the aviable options!\n +,-,*,/")
"""
