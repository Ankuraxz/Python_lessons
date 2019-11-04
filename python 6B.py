# if and elif works on boolean input
"""
if True
elif True """
"""  

!: LOgical Not 

if 3 !=0:

"""

# multiple decisions and the results of decision depends on result of previous decision

# WAP TO CHECK IF A PERSON IS ADULT, {IF YES IS HE/SHE EARNING, IF YES PRINT(" PAY TAX"): ELSE PRINT(" NO TAX")} ELSE PRINT NOT ADULT
age = int(input(" Enter age"))
# earn_status = input("press y for yes and n for no")
if age>=18:
  earn_status = input("press y for yes and n for no in response to your earning status")
  earn_status = earn_status.lower() #.upper()
  # print( earn_status)
  if earn_status == 'y':
    print("pay tax")
  elif earn_status == 'n':
    print("no tax")
  else:
    print(" Wrong Input")
    exit
else:
  print(" Not adult")
