# Thanks for visiting my code. This is a Student Management Program
# I did it with minimal use of tools and resources without functions and OOPS.
# as a Computer Science Project
# Suggest updates if required https://github.com/vyasrudra/basic-student-managementprogram
# time consumed [00h:33m:47s], can run in terminal
# $Rudra Vyas


studentdict = {
    "Rudra": {"Class": "11 A", "Roll Number": 22},
    "Kaushik": {"Class": "12 B", "Roll Number": 34},
    "Anmol": {"Class": "9 C", "Roll Number": 18},
}

program_continue = "y"

while program_continue == "y":
    print("1.) Add a Student")
    print("2.) Remove a Student")
    print("3.) Edit a Student")
    print("4.) View a Student")
    print("5.) List of Students")
    choice = int(input("Enter the Choice: "))
    if choice == 1:
        namestudent = input("Enter the Name of Student: ")
        classstudent = input("Enter the Class of Student: ")
        rollnumberstudent = input("Enter the Roll Number of Student: ")
        studentdict[namestudent] = {"Class": classstudent, "Roll Number": rollnumberstudent}
        print('New Student "', namestudent, '" Added.')
    elif choice == 2:
        delstudent = input("Enter the Student Name: ")
        try:
            del [studentdict[delstudent]]
            print("Student Deleted Successfully.")
        except KeyError:
            print("No Student Found")
    elif choice == 3:
        oldname = input("Enter the the Name: ")
        oldclass = input("Enter the the Class: ")
        oldrollno = input("Enter the the Roll Number: ")
        if oldname in studentdict.keys():
            editedname = input("Enter the the New Name: ")
            editedclass = input("Enter the the New Class: ")
            editedrollno = input("Enter the the New Roll Number: ")
            studentdict[oldname] = editedname
            studentdict[oldclass] = editedclass
            studentdict[oldrollno] = editedrollno
            print('"', oldname, '" Edited to "', editedname, '"Successfully.')
        else:
            print("No Student Found, Something Went Wrong.")
    elif choice == 4:
        viewname = input("Enter the Name of Student: ")
        if viewname in studentdict.keys():
            print(studentdict[viewname])
        else:
            print("No Student Found, Something Went Wrong.")
    elif choice == 5:
        viewliststudent = list(studentdict.items())
        for i in viewliststudent:
            print(list(i))
    else:
        print("Invalid Input")

    program_continue = input("Do you Wish to Continue[y/n]: ")

print("Program Terminated")
print("Created By Rudra Vyas, Class 11 A, Roll Number 22")
print("KV ONGC Chandkheda")
