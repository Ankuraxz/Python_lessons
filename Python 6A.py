# if #single decision and a single result
# WAP to check if a person is a adult or not (IS eligible to vote or not)
age = int(input(" Enter the age"))

if age >= 18:
  print("Eligible to vote")
  
# if-else pair # Single Decision but 2 results
# WAP to check if a person is a adult or not (IS eligible to vote or not)
age = int(input(" Enter the age"))

if age >= 18:
  print("Eligible to vote")
else:
    print("Not elligible")

# if-elif-else Multiple Decision, Multipe results
# WAP to check if a person is a adult or child or teen or old
age = int(input(" Enter the age"))
# elif is else if
if 18<=age<60:
  print("Adult")
elif 13<age<18:
    print("teen")
elif age>=60:
        print("old")
else:
  print("child")
  
