
#                           STUDENT RIGISTRATION FORM BASIC CODE

students = {None}
rolNum = {None}
Chk_and_Entery = input("\nIf You Want New Student Entery Please Press E: ")
if Chk_and_Entery=="e":
    print('''\nPlease Enter The Course Name From This List\nFor example: ai,IoT
        \nAI\nIoT\nBLOCKCHAIN\nCLOUDE COMPUTING\nWEB 3.0''')
    CoursList = input("Enter Course Name. ").split(",")
    rolNum = int(input("Enter Roll Number: "))
    name = input("enter your name: ").capitalize()
    age = int(input("enter your age: "))
    edu = input("entr your education: ").capitalize()
    students = {
    rolNum:{"Student_ID":f"{rolNum}",
            "Student Name":f"{name}",
            "Age":f"{age}",
            "Education":f"{edu}",
            "Course":f"{CoursList}"
            }
}

    print(students[rolNum])
else:
    print("Wrong Value")
