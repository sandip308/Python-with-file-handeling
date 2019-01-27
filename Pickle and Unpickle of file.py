import pickle
import Empdata
f=open("EMP DETAILS.txt",'wb')
n=int(input("How many employee do u have in your company"))
for i in range(n):
    id=int(input("Enter employee id "))
    name=input("Enter employee name ")
    salary=eval(input("Enter employee salary"))
    e=Empdata.EMP(name,id,salary)
    pickle.dump(e,f)
f.close()
f = open("EMP DETAILS.txt", 'rb')
print("Employee Details:---->")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("Reach end of the file")
        break
f.close()

