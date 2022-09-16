"""
▪ Try to write a new Program that takes at least four different
inputs
▪ Two of these inputs should be numbers
▪ Print out the handed over string variables
▪ Let the program do at least two different mathematical
operations (+ or – or * or /) with the numbers and print out
the results of these operations
"""

#input data
no1_in = input("Give me the first number:\n")
no2_in = input("Give me your number:\n")
name_in = input("Who are you?\n")
location_in = input("Where are you?\n")


#printing types of variables
print("printing types of variables")
print(no1_in, "is an", type(no1_in))
print(no2_in, "is an", type(no1_in))
print(name_in, "is an", type(no1_in))
print(location_in, "is an", type(no1_in))

#casting numbers in Float
print()
print("#casting numbers in Float")
no1_in_f = float(no1_in)
no2_in_f = float(no2_in)
print (no1_in_f, "is now an", type(no1_in_f))
print (no2_in_f, "is now an", type(no2_in_f))

#do some maths!
print("\nDo some maths")
print(no1_in, "-", no2_in, "=", no1_in_f-no2_in_f)
print("without prev casting")
print(float(no1_in)-float(no2_in))
print()
print(no1_in, "+", no2_in, "=", no1_in_f+no2_in_f)
print("without prev casting")
print(float(no1_in)+float(no2_in))
