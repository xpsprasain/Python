# while True:
#     try:
#         x= (int(input("Please enter a string")))
#         break
#
#     except ValueError:
#
#        print("Oops !! That was a invalid string")

# try:
#     x=int(input("ENter a number"))
# except ValueError:
#   print("Oops !! That was a invalid number")
# finally:
#     print("Last Block")


num=input("enter a number to divide: ")
try:
    if(int(num)<12):
        raise Exception("Number less than 12") 
    a=int(num) / 0

except ZeroDivisionError:
    print("can't divide by zero")

except TypeError:
    print("type mismatch")

except Exception:
    print("custom exception caught")
else:
    print("result is %f" %(a))
finally:
    print("executes always")