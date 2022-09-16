"""
▪ Adjust your program you wrote for Exercise 03 by using the
different shortcuts you learned
"""

#input data
no1_in = input("Give me the first number:\n")
no2_in = input("Give me your number:\n")
no3_in = input("Give me my number:\n")
no4_in = input("Give me your luckly number?\n")

res1=float(no1_in)+float(no2_in)
res2=float(no1_in)-float(no2_in)
res3=float(no1_in)*float(no2_in)
res4=float(no1_in)/float(no2_in)

res1+=1
res2-=1
res3*=1
res4/=1

print("\nresults:")
#print(res1,res2,res3,res4)
print(res1,"|",res2,"|",res3,"|",res4)

"""
#trash I tried some stuff
print("No1 = No1 + 1 = ", float(no1_in)+1)
print("\nSubtraction:")
#print("No1 = No1 - 2 = ",float(no1_in)-=2)
print("\nMultiplication:")
print(f"No1 = No1 * No2 = {float(no1_in)}"*=f"{float(no2_in)}")
print("\nDivision:")
print(f"No1 = No1 / No2 = {float(no1_in)}/={float(no2_in)}")
"""
