# User Input
name = input()
# By default String Input

name_2 = input("Enter your name")

print("Hi" +' '+ name +" or "+ name_2)

print(type(name))

# INPUTTING A NUMBER....YET A STR
 
num = input("Enter a number")

print(type(num))
"""
# Only string and char can be added (concatenated) in print fxn : # Finally mix up printing
# ONLY IF ALL TO BE PRINTED are <str> or <char> TYPE
a = "8"

print("A"+" is"+' a'+' variable'+ """ whose value is """+a)
"""

#Converting Decimal '10' to various number systems


print(0o10) # Octal ..... 


print(0x10) # Hexadecimal....


print(0b10) # Binary...


print(0o1) # Octal ..... 


print(0x1) # Hexadecimal....


print(0b1) # Binary...

#Python interprets a sequence of decimal digits without any prefix to be a decimal number:


type(10)

type(0o10)

type(0x10)

# eg.

a = 4.20
print(a)
print(type(a))


b =42000000000.0
print(b)
print(type(b))
# can also be written as

b1 = 4.20e10
print(b1)
print(type(b1))

# can also be written as
b2 = 4.20E10
print(b2)
print(type(b2))

# can also be written as
b3 = 4.20*(10**10)
print(b3)
print(type(b3))

#1.79e308


1.8e308


c = 2+5j
print(c)
print(type(c))

