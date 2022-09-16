"""
▪ Write a program that asks the user their name, if they enter
your name say "That is a nice name", if they enter "John
Cleese" or "Michael Palin", tell them how you feel about
them ;), otherwise tell them "You have a nice name."
"""
#here the user can change their name.
my_name = "Thomas Engler"

#input a name
name = input("What's your name?\n")

#if name == "Thomas Engler":
if name == my_name:
    print("You have a nice name!")

elif name == "John Cleese":
    print("I hate all your movies!")

elif name == "Michael Palin":
    print("You have never been funny!")

else:
    print("You have a nice name!")
