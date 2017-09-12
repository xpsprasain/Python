# ----------------------1-----------------------------------
# def length(object):#Define the length calculation function
#
#     count = 0  #initializing the length to be equal to zero
#     object = input("Enter the string: ") #enter the argument
#
#     for i in object:
#         count=count+1
#
#     print("Length of the string is "+str(count))
#
# length(object)


# ----------------------2-----------------------------------
# def vowel_count(object):
#     vowels = ['a','e','i','o','u']
#     object = input('enter the letter: ')
#
#     if object in vowels:
#         return "y"
#
#     else:
#         return "n"
#
# print(vowel_count(object))

# ----------------------3-----------------------------------
# def integer(object):
#     num = input("enter numbers (0-9) using commas: \n")
#     print(num.split(','))
#     print(tuple(num.split(',')))
#
#
# integer(object)


# ----------------------4-----------------------------------
# def is_palindrome(object):
#     object = input("Enter the string: \n")
#     for i, char in enumerate(object):
#         if char != object[-i - 1]:
#             return False
#         return True
#
#
# print(is_palindrome(object))


# ----------------------4-----------------------------------
# We are taking input from the user.
# Then in the function we are reversing the input i.e a using
# slice     [::-1] and
# storing in b
# It is palindrome if both a and b are same.

# def palin(object):
#     object = input("Enter to check palindrome: \n")
#     # Extended Slices to reverse order.
#     b = object[::-1]
#     if object == b:
#         return "True"
#     else:
#         return "False"
#
#
# palin(object)

# ----------------------5----------------------------------
# n = int(input("Enter the number of students: "))          #n is the number of items you want to enter
# d ={}
# print("Format be like: \n")
# print("{'Student_name1': mark1,Student_name2': mark2, ....... }\n")
# for i in range( n):
#
#     names = str(input("Enter the names of students: "))
#     marks = int(input("Enter the mark of students: "))
#
#     details = (names, marks)
#
#     if marks > 40:
#         d[details[0]] = details[1]
#
# print(d)


# ----------------------6----------------------------------


import math


x = [0,30,45,60,90,120,180,270,360]

y = list(map(lambda x: math.sin(x),x))

print(y)
