students = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78
}

while True:
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Show All Students")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = int(input("Enter student grade: "))

        if name in students:
            print("Student already exists!")
        else:
            students[name] = grade
            print("Student added successfully \n")

    elif choice == 2:
        name = input("Enter student name: ")

        if name in students:
            grade = int(input("Enter new grade: "))
            students[name] = grade
            print("Grade updated successfully \n")
        else:
            print("Student not found!")

    elif choice == 3:
        print("Student Grades:")

        for name, grade in students.items():
            print(name, "-", grade)

        print("\n")
        

    elif choice == 4:
        print("Exiting...\n")
        break

    else:
        print("Invalid choice")


    