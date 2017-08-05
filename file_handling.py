# fp = open("new_test.txt","a")
# print(fp)
#
# fp.write("Sulav Prasain")
# fp.write("\n....again")
# fp.close()

# f=open("new_test.txt",'r+')
# print(f)
#
# f.write("\nxxxxxxxxxxxxxxxxxxx")
# f.read()
# f.close()

f=open("new_test.txt",'a+')
print(f.tell())
print(f.seek(4,0))
f.read()
f.close()


