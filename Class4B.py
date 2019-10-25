a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] #2-D list
print(a) 

# ALGO 1 Traversing or Accessing:
for sublist in a:
  print(sublist)

# alternatively

for i in range (len(a)):
  for j in range (len(a[i])):
    print(a[i][j], end=" ")
  print("\n")

# CREATING A RANDOM mXn 2-D array of user defined size and value ='0'

m = int(input("m"))
n = int(input("n"))
a = [[0 for j in range(n)] for i in range(m)] 

for sublist in a:
  print(sublist)

#.append()

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
a.append([5, 10, 15, 20, 25]) 
print(a) 


a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
a[0].extend([12, 14, 16, 18]) 
print(a) 

#.reverse()
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
a[2].reverse() 
print(a) 

"10 20 30 40 50".split() #Str-List

print(l)
print(type(l))
print(l[0])
print(type(l[0]))

num = [int(i) for i in l] # LIST COMPREHENSION

print(num)
print(type(num))

print(num[0])
print(type(num[0]))


l = input("Enter string")
l_1 = input("Enter string").split()
print(l)
print(type(l))
print(l_1)
print(type(l_1))

l_2 = [int(no) for no in input("Enter string").split()]

print(l_2)
print(type(l_2))


A = [5,7,8,7,1,2,4]
print(sum(A))
print(sorted(A))
# print(reversed(A))
print(max(A))
print(min(A))

A = [5,7,8,7,1,2,4]
B = [8,9,9,9,9,9,9]
print(cmp(A,B)) # WORKS IN PYTHON 2

