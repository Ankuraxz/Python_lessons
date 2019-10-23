#Mutable vs Immutable Objects in Python. ... Simple put, a mutable object can be changed after it is created, and an immutable object can't. Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable. Objects of built-in types like (list, set, dict) are mutable.
a = [5,10,15,20,25,30,35,40]

#a[2] = 15
print("a[2] = ", a[2])

#a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

#a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])


a = [1, 2.2, "ankur", 'a']
print(a)
print(type(a))
print(len(a))
# TRAVERSING ALGO
# to access nth element in list....Arr[n-1]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
for i in range (len(a)):
  print(a[i])

# CHANGE THE VALUE ALGO
a[1] = 2
a[0] = 3.4
print(a)

# equivalent to array




#int type list -1D int array
# a = [1,5,8,4,96,35,72,41,12,10,63]
# print(a)
# print(len(a))
# print(type(a))

# for i in range (len(a)):
#   print(a[i])

# # SEARCHING -LINEAR SEARCH ALGO
# n = int(input("Enter number to be searched"))
# flag =0
# for i in range (len(a)):
#   if a[i] == n:
#     print("%d is found at location %d"%(n,i+1))
#     flag =+1
# if flag ==0:
#   print("%d not found"%n)


# SLICING
# Arr[rowthi:rowthj]
# Arr{intial index: FInal index}......BY DEFAULT II= 0 and FI= len(Arr)
# print(a[1:10])

# REVERSING A LIST
# print(a[::-1])
A=[]
print(type(A))
# METHODS OF ADDING DATA
A.append(2) #extend
print(A)
A.append(3)
print(A)
# UNCOMMENT COMMAND TO TEST
#insert
A.insert(0,5)
print(A)
#pop  inverse append by default
# A.pop(2)
# print(A)
# A.remove(5)
# print(A)
# A.clear()
# print(A)
# A.sort()
# print(A)
# A.reverse()
# print(A)




