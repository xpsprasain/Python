# l= [1,2,3]
# new_list=[elem*2 for elem in l]
#
# print(new_list)

# l=[[1,2,3]]
# new_list=[elem*2 for elem in l]
# print(new_list)

l=[[1,2,3]]

nl1 = [elem*2 for i in l for elem in i]
print(nl1)

nl1 = [elem*2 for i in l for j in i for elem in i]
print(nl1)