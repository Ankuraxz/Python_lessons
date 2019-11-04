# loop is a command that is used to run a set of statements for a given time/iterations.
#wap to print "hello" 10 times

# Rather using a for loop
for i in range(1,11):  # 0:n-1 iteration or intial,final+1
  print(i,"hello")
  
# rather using a while loop: while loop is used to execute a block of statements repeatedly until a given a condition is satisfied. 
i =1
while (i!=11):
  print(i,"hello")
  i+=1
else:
  print("end")
  exit
# Infinite loops
# In OPENCV YOU WANT TO KEEP THE WEBCAM OPEN AND record a video
# i =0
# while i==0:
#   print("a")

while True: #infinite loop
  print("a")

l = ["a","b",123]
for i in range(len(l)):
  print(l[i])
  
l = ["a","b",123]
for i in range(len(l)):
  print(l[i])
  
 s="hello world! Its Siraj"
for i in s:
  print(i)
else:
  print("he is grt")
 
len(s)

for i in range (len(s)):
  print(s[i])
  
for i in range (0,10):
  # for j in range (i): # from 0,i
  #   print("*",end=" ")
  j=0
  while (j<=i):
    print("*",end=" ")
    j+=1
  print("\n")

# wap to print all consonants of a string
s = str(input(" enter string"))
s = s.lower()
for i in s:
  if i == 'a' or i=='e' or i=='i' or i== 'o' or i=='u':
    continue
  print(i)

# wap to break at 1st vowel
s = str(input(" enter string"))
s = s.lower()
for i in (s):
  if i == 'a' or i=='e' or i=='i' or i== 'o' or i=='u':
    print(" vowel detected  ")

    break
  print(i)
 
 # ascii('i')
# ref https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
#https://www.programiz.com/python-programming/examples/ascii-character

ord('i')

ord('a')

ord('z')

chr(122)

for i in range(97,123):
  print(chr(i),end=" ")
