# l=[1,2,3,4,5,6]
#
# for i in l:
#     print(l)



# for item in [1,2,3,4,5]:
#     if item ==3:
#         break
#     print(item)

# for i in range(1,20):
#         print(i, end='\t')



# def test():
#     return "Sulav"
#
# x=test()
# print(x)


# def test(msg="Sulav"):
#
# test()
# print()



# def test(*args,msg="Sulav"):
#     print("args"+str(args))
#     print("msg"+msg)
#
# test()
#
# test("a")
#
# test(1,2,4,msg="Message")


# def greet_me(**kwargs):
#     if kwargs is not None:
#         for key, value in kwargs.items():
#             print("%s=%s" % (key, value))
#
#
# greet_me(name="yahoo", age=18, add='ktm')


# d= {"name": "Sulav", "Age": 19}
#
# for value in d.values():
#     print("value" +","+str(value))

# mutable : replacing the object with same object
#inmutable: replacing thr object with another object


def modifyList(l):

    # l.extend(["newVal"])
    #works as a append after putting big bracket

    l.extend("newVal")
    # creates every string as new like "newVal" = 'n' ,'e'

    # l.append("newVal")


def modifyString(s):
    print("inside function: "+s.upper())

def modifyDict(d):
    d.update({"f": 6})

# dictionary is mutable



ls=[1,2,3]
ms="Hello"
d={"a":1, "b":2, "c":3}

print(ls)
print(ms)
print(d)

modifyList(ls)
modifyString(ms)
modifyDict(d)


print(ls)
print(ms)
print(d)

