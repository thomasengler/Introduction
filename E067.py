"""
▪ Use your knowledge of assigning Variables to declare at
least seven different variables in a new script
▪ Print out the variables and combine them with either strings
or each other by using commas and f-Strings
▪ Your program should contain at least 14 different print
commands
"""

# int
oven_temperature = 190
turn_steak_in_grad = 180

# string
greetings = "Servus"
steak_welldone = "well done"
steak_med = "medium"
steak_bloody = "bloddy"

# float
meat_conenstense = 125e12

# bool
fire_on = True
oven_open = True
oven_finished = False

#printing operations with f and ,
print(greetings, "@all")
print("The oven temperature is", oven_temperature)
print("When the owen temperature is", oven_temperature, "turn the steak by", turn_steak_in_grad, "grad")
print(f"How you would like your steak? {steak_welldone}, {steak_med} or {steak_bloody}")
print(f"The meat conenstense is {meat_conenstense} in tengl")

#bool testing
print("Is the fire on?", fire_on)
print("Is the oven really open?", oven_open)
print("Is the steak finished?", oven_finished)
print("End of script! Sooo" , fire_on, oven_open)
print("")

#f testing
printing = f"I already asked you! How you would like your steak? {steak_welldone}, {steak_med} or {steak_bloody}"
print(printing)

#cal
print(f"oven temperature lowered by 9 {oven_temperature-9} is ")
print(f"Just some stupid calculations {oven_temperature-turn_steak_in_grad}")


# just for my documentory
print("")
str_var1 = "hallo world"
str_var2 = "Thomas"
int_age = 36

print("My name is", str_var2,"and I am",int_age)
print(f"Learning python with {str_var1}")

printingX = f"Learning python with {str_var1}"
print(printingX)
#test without f format
print("")
print("What will happened without format f?")
printing2 = "My name is", str_var2,"and I am",int_age
print(printing2)
