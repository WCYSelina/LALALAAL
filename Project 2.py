# Example of data type:
# #1.integer
# 10
# 2.float
# 0.6
# #3.string
# 'Selina'
# example of usage of variable

# button=1
# button=2
# button = button + 1 #2+1 because the 2nd replaced the 1st, if 1+1 change the name of the variable
# print(button)       # or delete the same variable.

# abc = 1
# abc2 = abc
# abc2=2
# print(abc)

# check = 1
# if (check==1):
#     print(2)
# else:
#     print(1)
#
# print(3)

# while False:#exit condition
#     print(1)
#     print(2)
# print(3)
# print(4)
# print(5)

# n = 1
# while True:
#     n = n + 1
#     if n > 10:
#         break #immediately exit the loop
#     if n == 5:
#         continue #immeadiately create a new loop, in this case when n is 5, it immediately back to
#     print(n)     # above, hence 5 would not be printed.


# a = 0
# while a < 3:
#     a = a + 1
#     n = 0
#     while True:
#         n = n + 1
#         if n > 10:
#             break
#         if n == 5:
#             continue
#         print(n)

# Example of data type:
# #1.integer
# 10
# 2.float
# 0.6
# #3.string
# 'Selina'
# example of usage of variable

# button=1
# button=2
# button = button + 1 #2+1 because the 2nd replaced the 1st, if 1+1 change the name of the variable
# print(button)       # or delete the same variable.

# abc = 1
# abc2 = abc
# abc2=2
# print(abc)

# if statement

# check = 1
# if (check==1):
#     print(2)
# else:
#     print(1)
#
# print(3)

# while False:#exit condition
#     print(1)
#     print(2)
# print(3)
# print(4)
# print(5)

# n = 1
# while True:
#     n = n + 1
#     if n > 10:
#         break #immediately exit the loop
#     if n == 5:
#         continue #immeadiately create a new loop, in this case when n is 5, it immediately back to
#     print(n)     # above, hence 5 would not be printed.

#List
# []
# [1]
# a = [] #empty list
# b = [1]
# c = [1,2,3]
# d = [1,2.0,3,"haha"] # the list can be mixed with all number type
# print(a)
# print(b)
# print(c)
# print(d)
#
# print(c[0])
# print(d[3])
# print(type(a))
# a.append(1)
# print(a)
# a.append(2) # add items/elements into the list
# print(a)
# a.append(3)
# print(a)
#
# del a[0] # delete items/elements from the list
# print(a)
# del a[0]
# print(a)
# del a[0]
# print(a)
#
# del d[:] # delete items/elements all from the list
# print(d)

# del d[0:1] # delete items/elements at a range
# print(d)

# favourite_foods = ["katsu curry chicken don","sushi"]
# favourite_hobbies = ["sleeping","laying on the sofa and do nothing"]
# favourite = favourite_hobbies+favourite_foods
# print(favourite)

# equation = (25*3)+(2*40)
# print(equation)

# a = [1,2,3,4,5,6]
# print(max(a))
# print(min(a))

# a = ["abc","xyz","aba","1221"]
# exitcon = len(a)
# n=0
# m=0
#
# while n<exitcon:
#     if len(a[0]) >= 2:
#         if a[n][0] == a[n][-1]:
#             print("yes")
#             m = m + 1
#         else:
#             print("no")
#     else:
#         print("no")
#     n=n+1
#
# print(m)



# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# a = ['p','q']
# n = 5
# x = 1
# answer = []
#
# while x <= n :
#     b = (a[0] + str(x)) #str is to convert number into string
#     c = (a[1] + str(x))
#     x = x + 1
#     answer.append(b)
#     answer.append(c)
#
# print(answer)


# a = [0,1,2,3,4,5]
#
# answer = []
#
# b = a[0]+1
# c = a[1]-1
# d = a[2]+1
# e = a[3]-1
# f = a[4]+1
# g = a[5]-1
#
# answer.append(b)
# answer.append(c)
# answer.append(d)
# answer.append(e)
# answer.append(f)
# answer.append(g)
# print(answer)
#
# a = [0,1,2,3,4,5]
#
# answer = []
# n = 0
# while n < 5:
#     b = a[n]+1
#     c = a[n + 1]-1
#     n = n + 2
#     answer.append(b)
#     answer.append(c)
# print(answer)

# a = [0,1,2,3,4,5]
# answer = []
# n = 0
# while n < 5:
#     answer.append(a[n+1])
#     answer.append(a[n])
#     n = n + 2
# print(answer)



# Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

# a = [11,33,50]
# print(str(a[0])+str(a[1])+str(a[2]))

# a = [11,33,50]
# n = 0
# while n<len(a):
#     print(a[n],end="")
#     n = n + 1



# Write a Python program to split a list every Nth element.
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n = 3
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

# a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
#
#
# n = 2
# answer = []
#
# x = 0
# while x < n:
#     answer.append([])
#     x = x + 1
#
#
# x = 0
# z = 0
# while x < len(a) :
#     answer[z].append(a[x])
#     z = z + 1
#     x = x + 1
#
#     if z == n:
#         z = 0
#
# print(answer)

# a = 1 + 2
#
# b = 1
# c = 1
# d = b + c
# print(d)

# b = [1,2,3,4]
# c = [1,2,3,4]
#
# for x in b:
#     d = b[x]+c[x]
#     print(d)

# b = [1,2,3,4]
# c = [1,2,3,4]
#
# for x in range(len(b)): #similar to while loop
#     d = b[x]+c[x]
#     print(d)

# a = ["red", "orange", "green", "blue", "white"]
# c = "codeprenure"
# for x in range(len(c)):
#     print(x)

# b = 1
# c = 1
# d = b + c
# print(d)

# Function

# def addit(firstno,secondno):
#     d = firstno + secondno
#     print(d)
#     return d
#
# addit(1,1)
# addit(2,2)
# addit(3,3)
# addit(4,4)
# addit(5,5)
#
#
# def addit():
#     d = 2 + 3
#     print(d)
#     return d
#
#
# a = addit()
# b = addit()
#
# def addit():
#     d = 2 + 3
#     print(d)
#     return d
#
# a = addit()
# b = addit()

# Write a Python program to compute the difference between two lists
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

# color_A = ["red", "orange", "green", "blue", "white"]
# color_B = ["black", "yellow", "green", "blue", "pink", "white", "purple"]
# answer = []
#
# def abc(a,b):
#     del answer[:]
#     x = 0
#     while x < len(a):
#         z = 0
#         n = 0
#         while n < len(b):
#             if a[x] == b[z]:
#                 break
#             z = z + 1
#             n = n + 1
#             if z == len(b):
#                 z = -1
#                 answer.append(a[x])
#         x = x + 1
#
# abc(color_A, color_B)
# print("Color a - Color b = ",end="")
# print(answer)
# abc(color_B,color_A)
# print("Color b - Color a = ",end="")
# print(answer)



# def maxNumber(first_Number,second_Number,third_Number):
#
#     if first_Number > second_Number and first_Number > third_Number:
#         print(first_Number)
#         return first_Number
#     if second_Number > first_Number and second_Number > third_Number:
#         print(second_Number)
#         return second_Number
#     if third_Number > first_Number and third_Number > second_Number:
#         print(third_Number)
#         return third_Number
#
# maxNumber(1,2,3)
# maxNumber(1,4,3)
# maxNumber(5,4,3)

# inputList = [8,2,3,10,7,5]
# def hello(listInput):
#     b = 0
#     c = 0
#     while b < len(listInput):
#         c = listInput[b] + c
#         b = b + 1
#     return c
#
# a = hello(inputList)
# print(a)

# 4.    Write a Python program to reverse a string.
# a.    Sample String : "1234abcd"
# b.    Expected Output : "dcba4321"

# a = "1234abcd"
#
# b = ""
# x = -1
# d = 0
# while d<len(a):
#     b = b + a[x]
#     x = x - 1
#     d = d + 1
# print(b)

# 5.    Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# a.    Sample String : 'The quick Brow Fox'
# i.    Expected Output :
# ii.    No. of Upper case characters : 3
# iii.    No. of Lower case Characters : 12

# a = "The quick Brow Fox"
#
# def lwcase(s):
#     x = 0
#     c = 0
#     d = 0
#     while(x < len(a)):
#         if(s[x].isupper()):
#             c = c + 1
#         elif(s[x].islower()):
#             d = d + 1
#
#         x = x + 1
#     print(c)
#     print(d)
#
# b = lwcase(a)

# 6.    Write a Python function that takes a list and returns a new list with unique elements of the first list.
# a.    Sample List : [1,2,3,3,3,3,4,5]
# b.    Unique List : [1, 2, 3, 4, 5]

# a = [1, 2, 3, 3, 3, 3, 4, 5]
#
# def dup(s):
#     d = 0
#     x = 0
#     newList = []
#
#     while x < len(s):
#         if s[x] not in newList:
#             newList.append(s[x])
#         x += 1
#
#     return newList
# b = dup(a)
# print(b)

# Write a Python function that takes a number as a parameter and check the number is prime or not.
# a. Note: A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than one and itself.

# c = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
#  113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
#  251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
#  397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547,
#  557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
#  701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
#  863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
#
# def prime(pa):
#
#     a = -1
#
#     if pa < 2:
#         a = False
#     else:
#         for i in range(2,pa):
#             if pa % i == 0:
#                 a = False
#                 break
#         if a == -1:
#             a = True
#     return a
# # b = prime(6)
# # print(b)
#
# answer = []
# for y in range(0,1000):
#     print(y)
#     if prime(y) == True:
#         answer.append(y)
# print(len(answer))
#
# for l in answer:
#     if l not in c:
#         print(l)

# Write a Python program to print the even numbers from a given list.
# a. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b. Expected Result : [2, 4, 6, 8]

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def even(counter):
#     b = []
#     while counter < len(a):
#         if(a[counter]%2==0):
#             b.append(a[counter])
#         counter+=1
#     return b
# c = even(0)
# print(c)

# Write a Python program to print the following string in a specific format (see the output).
# a.    Sample String: "Twinkle, Twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, Twinkle, little star, How I wonder what you are"
# b.    Output :
# i.    Twinkle, Twinkle, little star,
# ii.        How I wonder what you are!
# iii.            Up above the world so high,
# iv.            Like a diamond in the sky.
# v.    Twinkle, Twinkle, little star,
# vi.        How I wonder what you are

# a = "Twinkle, Twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, Twinkle, little star, How I wonder what you are"
#
# b ='''Twinkle, Twinkle, little star,
#            How I wonder what you are!
#                 Up above the world so high,
#                Like a diamond in the sky.
# Twinkle, Twinkle, little star,
#          How I wonder what you are'''
# print(b)

# 2.    Write a Python program to display the current date and time.
# a.    Sample Output :
# i.    Current date and time : 2014-07-05 14:34:14

# import time #import the modulus
# print(dir(time)) #show all the method that can be used from the modulus
# print(help(time.ctime)) #details of the modulus
# print(time.ctime(4))
# print(help(time.ctime))
# print(time.ctime())

# 3.    Write a Python program that accepts the user's first and last name and print them in reverse order with a space between them.
# a.    Sample query input:
# i.    Enter your first name: ALI
# ii.    Enter your last name: Bakar
# b.    Sample Output
# i.    Your name is Bakar ALI

# firstName = ""
# firstName = input("Enter your first name: ")
# lastName = ""
# lastName = input("Enter your last name :")
# print(lastName,firstName)
#

# x = input("Enter the first number: ")
# y = input("Enter the second number: ")
# z = int(x)+int(y)
# print("Adding "+str(x)+" and "+str(y)+" is equal to: "+str(z)) # int(string) convert integer from string



# a = [1,2,3,4]
# b = (2,3,4,5,6)
# c = (1)
# d = (1,)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# # read
# print(a[1])
# print(b[1])
# # write
# a[0]=9
# print(a)
# # b[0]=9
# # print(b)
# # add item
# a.append(99)
# print(a)
# b = b +(99,)
# print(b)

# 5.    Write a Python program that accepts a sequence of comma-separated numbers from the user and generate a list and a tuple with those numbers.
# a.    Sample data : 3, 5, 7, 23
# b.    Output :
# i.    List : ['3', ' 5', ' 7', ' 23']
# ii.    Tuple : ('3', ' 5', ' 7', ' 23')

# n = 0
# a = input("write: ")
# print(a)
#
# b = []
# while n < len(a):
#     # if(a[n]!=","):
#     #     b.append(a[n])
#     # n+=1
#     if a[n]==",":
#         pass
#     elif (n == 0) or (a[n-1]== ","):
#         b.append(a[n])
#     elif a[n-1] != ",":
#         b[-1] = b[-1] + a[n]
#     n+=1
# print(b)


# b = [x,z]
# c = (x,z)
#
# print(b)
# print(c)

# 6.    Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# a.    Sample value of n = 5
# b.    Expected Result: 5+55+555 = 615

# def function(a):
#     a = str(a)
#     z = a + a
#     l = a + a + a
#     c = int(a) + int(z) + int(l)
#     return c
#
# b = function(5)
# print(b)

# 7.    Write a Python program that accepts an integer (n) and computes the value of:
# a.    Sample value of n = 5
# b.    Expected Result: 5 + (5 x 5) + (5 x 5 x 5) = 155

# def function(a):
#     c = a+(a*a)+(a*a*a)
#     return c
#
# b = function(5)
# print(b)

# 8.    Write a Python program to calculate the number of days between two dates.
# a.    Use this line to help you (datetime module)
# i.    From datetime import date
# b.    Sample dates : (2014, 7, 2), (2014, 7, 11)
# c.    Expected output: 9 days

# from datetime import datetime
# # import time
# # # import datetime
# # # print(datetime.now())
# # # a = datetime.now()
# # # b = datetime.date(a)
# # # print(b)
# #
# # a = datetime(2014,7,11)-datetime(2014,7,2)
# # print(a.days,"days")

# Write a Python function to get the volume of a sphere with a radius of 6.
# The formula to get the volume of a sphere is shown below.
# V=4/3 πr^3

# import math
# print(dir(math))
# def equation(radius):
#     V=(4/3)*(math.pi)*math.pow(radius,3)
#     return V
# b = equation(6)
# print(b)

# 10.Write a Python program to get the difference between a given number and 17.
# If the number is greater than 17, return double the difference; otherwise, return the absolute difference.

# def number(a):
#     v = a - 17
#     if a>17:
#         v*=2
#     else:
#         v=-v
#     return v
# b = number(14)
# print(b)

# 11.Write a Python program to calculate the sum of three given numbers.
# If the values of three given numbers are equal, then return three times their sum.

# def sum(a,b,c):
#     if a == b and a == c:
#         b = (a+a+a)*3
#     else:
#         b = a + b + c
#     return b
# d = sum(5,5,5)
# print(d)
#
# def sum2(a,b,c):
#     suma=a+b+c
#     if a==b and b == c:
#         suma*=3
#     return suma
#
# print(sum2(5,5,5))

# 12.Write a program that prints out all the elements of the list that are less than 5.
# a. Sample List
# i. List1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b. Extras:
# i. Instead of printing the elements one by one, make a new list with all the elements less than 5 from this list and print out this new list.
# ii.Ask the user for a number and return a list that contains only elements from the original list that are smaller than that number given by the user.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# def d(f):
#     i = 0
#     g = input("What num")
#     del b[:]
#     while i<len(f):
#         if f[i]<int(g):
#             b.append(f[i])
#         i+=1
#     return b
# c = d(a)
# print(c)
#
# c = d(a)
# print(c)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# def d(f):
#     inputA = input("Insert a number : ")
#     l = []
#     for i in f:
#         if i < int(inputA):
#             l.append(i)
#     return l
#
# print(d(a))

# 13.    Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is", return the string unchanged.
# a.    Sample input: "isEmpty"
# b.    Output : “isEmpty”
# c.    Sample input2: “Outside”
# d.    Output2: “isOutside”
# e.    Sample Input3: “IsInside”
# f.    Output2: “IsInside”

# a = "isEmpty"
# b = "Outside"
# c = "IsInside"
#
# def str(s):
#     g = "is"
#     print(s[0])
#     if s[0] != 'I' and s[0] != 'i':
#         print(s[1])
#         if s[1]!= "S" and s[1]!= "s":
#             g += s
#             return g
#     else:
#         return s
#
# d = str(a)
# e = str(b)
# f = str(c)
# print(d)
# print(e)
# print(f)

# 14.    Write a Python program to get a string and n (non-negative integer). Make n copies of a given string.
# a.    Example 1:
# i.    Input String: “.test”
# ii.    Input N: 3
# iii.    Output: “.test.test.test”
# b.    Example 2:
# i.    Input String: "Helloo"
# ii.    Input N: 5
# iii.    Output: “HellooHellooHellooHellooHelloo”

# a = input("Write any words: ")
# b = input("num of copies: ")
#
# def ss(aa,bb):
#     f = ""
#     for i in range(int(bb)):
#         f = f+aa
#     return f
#
#
# c = ss(a,b)
# print(c)

# 15.    Write a Python program to find whether a given number (accept from the user) is even or odd. Print out an appropriate message to the user.
# a.    Example 1:
# i.    Input: 5
# ii.    Output: It is an odd number

# a = input("Write a num: ")
# def q(qq):
#     c = ""
#     if int(qq)%2 == 0:
#         c = "even"
#     else:
#         c = "odd"
#     return c
#
# b = q(a)
# print(b)

# 16.    Write a Python program to count the number 4 in a given list
# a.    Example 1:
# i.    Input List: c
# ii.    Output Interger: 3

# a = [1,4,5,6,4,8,6,4]
#
# def count(k):
#     counter = 0
#     for i in range(len(k)):
#         if k[i] == 4:
#             counter+=1
#     return counter
# b =count(a)
# print(b)

# 17.    Write a Python program to get the n (non-negative integer) copies of the first two characters of a given string. Return the n copies of the whole string if the length is less than 2
# a.    Example 1:
# i.    Input string: "abcdef"
# ii.    Input integer number of copy: 3
# iii.    Output string: "ababab"
# b.    Example 2:
# i.    Input String: "a"
# ii.    Input integer No of copy: 5
# iii.    Output string: "aaaaa"

# a = input("Write a words: ")
# b = input("num of copies: ")
# def check(l,k):
#     g = ""
#     for i in range(int(k)):
#         if len(a) < 2:
#             g += l[0]
#         else:
#             g += l[0] + l[1]
#     return g
#
# c = check(a,b)
# print(c)

# 18.    Write a Python function to test a user input whether the inputted letter is a vowel or not.
# a.    Input from user: “please insert a letter:”
# b.    Output1: the letter is a vowel
# c.    Output2: the letter is not a vowel

# a = input("Write an alphabet: ")
#
# def alp(d):
#     c = ["a","e","i","o","u"]
#     e = ""
#     for i in range(len(c)):
#         if d == c[i]:
#             e = "the letter is a vowel"
#             return e
#         # else:
#         #     e = "the letter is not a vowel"
#     return "the letter is not a vowel"
# b = alp(a)
# print(b)

# 19.    Write a Python program to check whether a specified value is contained in a group of values.
# a.    Test Data :
# i.    3 -> [1, 5, 8, 3] : True
# ii.    -1 -> [1, 5, 8, 3] : False

# a = [1, 5, 8, 3]
# def check(integer):
#     n = input("Enter a number: ")
#     for i in range (len(integer)):
#         if integer[i] == int(n):
#             return"True"
#     return"False"
# f=check(a)
# print(f)

# 20.    Write a Python program to create a histogram from a given list of integers
# a.    Sample Input: [2, 3, 6, 5]
# b.    Sample Output:
# i.    **
# ii.    ***
# iii.    ******
# iv.    *****

# a = [2, 3, 6, 5]
# def his(gram):
#     s = ""
#     for i in range(len(gram)):
#         n = 0
#         while n<gram[i]:
#             s += "*"
#             n+=1
#         s += "\n"
#     return s
# d = his(a)
# print(d)

# 21.    Write a Python program to print all even numbers from a given numbers list in the same order and stop printing any numbers that come after 237 in the sequence.
# a.    Sample numbers list :
# i.    numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#                   399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#                   815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527 ]
# numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#           399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#           815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527 ]
#
# def even(num):
#     s = []
#     for i in range(len(num)):
#         if(num[i]==237):
#             return s
#         else:
#             if(num[i]%2==0):
#                 s.append(num[i])
# d = even(numbers)
# print(d)
duwhduwdhuwdhuwhdu

