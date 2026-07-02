# Student Data Organizer

students = []
all_subjects = set()

while True:
    print("\n========== Student Data Organizer ==========")
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Subjects")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("\n--- Add New Student ---")

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")

        subjects_input = input("Enter subjects (comma-separated): ")
        subjects = [sub.strip() for sub in subjects_input.split(",")]

        all_subjects.update(subjects)

        student_id = input("Enter student ID: ")
        dob = input("Enter date of birth (DD-MM-YYYY): ")

        student_identity = (student_id, dob)

        student_record = {
            "identity": student_identity,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student_record)

        print(f"\nStudent '{name}' added successfully!")

    elif choice == "2":
        print("\n--- All Student Records ---")

        if not students:
            print("No student records found.")
        else:
            for student in students:
                sid, dob = student["identity"]

                print("------------------------------")
                print(f"Student ID : {sid}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Grade      : {student['grade']}")
                print(f"Subjects   : {', '.join(student['subjects'])}")
                print(f"DOB        : {dob}")
                print("------------------------------")

    elif choice == "3":
        print("\n--- Update Student Information ---")

        sid = input("Enter student ID to update: ")
        found = False

        for student in students:
            if student["identity"][0] == sid:
                found = True

                print("\n1. Update Age")
                print("2. Update Subjects")

                option = input("Choose option: ")

                if option == "1":
                    student["age"] = int(input("Enter new age: "))
                    print("Age updated successfully.")

                elif option == "2":
                    new_subjects = input("Enter new subjects (comma-separated): ")
                    subjects_list = [s.strip() for s in new_subjects.split(",")]

                    student["subjects"] = subjects_list
                    all_subjects.update(subjects_list)

                    print("Subjects updated successfully.")

                else:
                    print("Invalid option.")

                break

        if not found:
            print("Student ID not found.")

    elif choice == "4":
        print("\n--- Delete Student ---")

        sid = input("Enter student ID to delete: ")
        found = False

        for i, student in enumerate(students):
            if student["identity"][0] == sid:
                del students[i]
                found = True
                print("Student record deleted successfully.")
                break

        if not found:
            print("Student ID not found.")
    elif choice == "5":
        print("\n--- Subjects Offered ---")

        if not all_subjects:
            print("No subjects available.")
        else:
            for subject in sorted(all_subjects):
                print(subject)
    elif choice == "6":
        print("\nThank you for using the Student Data Organizer!")
        break
    else:
        print("Invalid choice. Please try again.")