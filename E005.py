"""
▪ Write a program that asks for two numbers
▪ If the sum of the numbers is greater than 100, print "That is
a big number.“
▪ If the sum is greater than 10, print “That is a mediocre
number.”
▪ If the sum is greater than 5, print “That is a small number”
▪ In all other cases print “This is a very small number”
▪ Combine all predicates in one if, elif, else statement
"""

#input two numbers
no1 = float(input("First number?\n"))
no2 = float(input("Second number?\n"))

#calculations
res1 = no1 + no2
print("The sum of your numbers", no1,"and", no2, "\nis", res1)

if res1 > 100:
    print("That is a big number.")

elif res1 > 10:
    print("That is a mediocre number.")

elif res1 > 5:
    print("That is a small number.")

else:
    print("This is a very small number.")
