"""
Group Exercise 01 – More complex calculations
#############################################
▪ Each group should write a program that asks the user for at
least 10 different numbers, they have to be floating point
numbers and integers
▪ Run at least 35 different mathematical operations with these
numbers, 5 for each of the seven you used in Exercise 03
▪ Print out the results using either f-Strings or commas in
your print commands
"""
#User input
print("# Put 10 different numbers!\n# The first three should be integers the rest can be floating point numbers")
no1 = int(input("Give me the first number:\n# It should be an integer!\n"))
no2 = int(input("Give me the second number:\n# It should be an integer!\n"))
no3 = int(input("Give me the third number:\n# It should be an integer!\n"))
no4 = float(input("Give me the fourth number:\n"))
no5 = float(input("Give me the fifth number:\n"))
no6 = float(input("Give me the sixth number:\n"))
no7 = float(input("Give me the seventh number:\n"))
no8 = float(input("Give me the eighth number:\n"))
no9 = float(input("Give me the ninth number:\n"))
no10 = float(input("Give me the tenth number:\n"))

#calculations

#Addition
add1 = no1+no2
add2 = no3+no4
add3 = no5+no6
add4 = no6+no10
add5 = no7+no8+no9+no10

#Subtraction
sub1 = no1-no2
sub2 = no3-no4
sub3 = no5-no6
sub4 = no6-no10
sub5 = no7-no8-no9-no10

#Multiplication
mul1 = no1*no2
mul2 = no3*no4
mul3 = no5*no6
mul4 = no6*no10
mul5 = no7*no8*no9*no10

#Division
div1 = no1/no2
div2 = no3/no4
div3 = no5/no6
div4 = no6/no10
div5 = no7/no8/no9/no10

#Integer Division
int1 = no1//no2
int2 = no3//no4
int3 = no5//no6
int4 = no6//no10
int5 = no7//no8

#Power
pow1 = no1**no2
pow2 = no3**no4
pow3 = no5**no6
pow4 = no6**no10
pow5 = no7**no8

#Remainder
rem1 = no1%no2
rem2 = no3%no4
rem3 = no5%no6
rem4 = no6%no10
rem5 = no7%no8

#Output via print() with commas or f-strings
print("\n####################\n Results")

print("\n Addition:")
print("no1+no2=",add1)
print("no3+no4=",add2)
print("no5+no6=",add3)
print("no6+no10=",add4)
print("no7+no8+no9+no10=",add5)

print("\n Subtraction:")
print("no1-no2=",sub1)
print("no3-no4=",sub2)
print("no5-no6=",sub3)
print("no6-no10=",sub4)
print("no7-no8-no9-no10=",sub5)

print("\n Multiplication:")
print("no1*no2=",mul1)
print("no3*no4=",mul2)
print("no5*no6=",mul3)
print("no6*no10=",mul4)
print("no7*no8*no9*no10=",mul5)

print("\n Division:")
print("no1/no2=",div1)
print("no3/no4=",div2)
print("no5/no6=",div3)
print("no6/no10=",div4)
print("no7/no8/no9/no10=",div5)

print("\n Integer Division:")
print("no1//no2=",int1)
print("no3//no4=",int2)
print("no5//no6=",int3)
print("no6//no10=",int4)
print("no7//no8=",int5)

print("\n Power:")
print("no1**no2=",pow1)
print("no3**no4=",pow2)
print("no5**no6=",pow3)
print("no6**no10=",pow4)
print("no7**no8=",pow5)

print("\n Remainder: %")
print("no1%no2=",rem1)
print("no3%no4=",rem2)
print("no5%no6=",rem3)
print("no6%no10=",rem4)
print("no7%no8=",rem5)
