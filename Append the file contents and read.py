f=open("My 1st file.txt",'a+')
print("Enter more text ")
str=input()
f.write(str)

print("Writing in a file successfully")
f.seek(0,0)
print("The file contents are: ")
print(f.read())
f.close()