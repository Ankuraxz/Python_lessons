"Hello World!"
print(" Hello world")

10
10.09
09.89

# Single Line Comment

""" Multi Line Comment

abcdefgh


kk

kkk


"""


# spacing and stuff
print("Hello \nWorld")
print("Hello \tWorld")
print("Hello \aWorld") # Audio in C/Cpp



#print()
# Print FXN
print("Hello World")
a =9.0
b =9
print(a)
print(type(a))
print(b)
print(type(b))

# Formatting
print("%s is %s country"% ("India", "My"))
print("%s %s is my name"%("Ankur" ,"verma"))
print("%d is my roll number"% (251701105))

print("%f is my cgpa"% (8.00))
print("%.2f is my cgpa"% (8.00001))
print("%.8f is my cgpa"% (8.00))

print("%c is my initials"%('A'))

# Yet Another way .....no problem of data type....UNIVERSAL FORMATTING
print("{} is {} country and I love it {} i.e. a percentage of  {}{}".format("India", "My", 3000, 500.000,"%")) # 500.000 printed as 500.0...smart af
print("{} is {} country and I love it {} i.e. a percentage of  {}{}".format("India", "My", 3000, 500.00100,"%")) # Most Significant Digit

print(" I love my {}".format("INDIA"))

# END and SEP
print("HEllo world", end =" LOVE ")
print("HEllo world")

A=10
B='rat'
print("A","B", B, A, "ABC") # Same Line Print

print("A","B", B, A, "ABC", sep=(" \n"))# V.IMP

#Printing a variable value

a = 874

print(a)
print("a")

# Finally mix up printing
# ONLY IF ALL TO BE PRINTED are <str> or <char> TYPE
a = "8"

print("A"+" is"+' a'+' variable'+ """ whose value is """+a)
