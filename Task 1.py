dict = {}
a = int(input("Enter the number of students: "))

for i in range(1,a+1):
    name = input("Enter the student's name: ")
    marks = float(input("Enter the marks of the student: "))
    dict[name] = marks

n = input("\n\nEnter the student's name: ")

if(n in dict):
    print("{}'s marks: {}".format(n,dict[n]))
else:
    print("Student not found.")