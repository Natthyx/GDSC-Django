# Student Database Program

# Initialize an empty dictionary to store student information
student_database = {}

def add_student():
    student_id = input("Enter student ID: ").upper()
    Fname = input("Enter student first name: ").capitalize()
    Lname = input("Enter student last name: ").capitalize()
    Year = int(input("Enter student Year: "))
    Department = input("Enter student Department: ")

    # Create a dictionary to store student details
    student_details = {'ID': student_id, 'First Name': Fname,'Last Name': Lname, 'Year': Year, 'Department': Department}

    # Add the student to the database
    student_database[student_id] = student_details
    print(f"Student {Fname} with ID {student_id} added successfully!\n")

def view_student():
    student_id = input("Enter student ID to view details: ").upper()
    if student_id in student_database:
        student_details = student_database[student_id]
        print("\nStudent Details:")
        for key, value in student_details.items():
            print(f"{key}: {value}")
        print()
    else:
        print(f"Student with ID {student_id} not found in the database.\n")

def list_all_students():
    print("\nList of All Students:")
    for student_id, details in student_database.items():
        print(f"ID: {student_id}, Name: {details['First Name']} {details['Last Name']}, Year: {details['Year']}, Department: {details['Department']}")
    print()

def update_student():
    student_id = input("Enter student ID to update details: ").upper()
    if student_id in student_database:
        print(f"Update details for student with ID {student_id}:")
        student_id = input('Enter updated Student ID').upper()
        Fname = input("Enter updated First Name: ").capitalize()
        Lname = input("Enter updated Last Name: ").capitalize()
        Year = int(input("Enter updated Year: "))
        Department = input("Enter updated Department: ")

        # Update student details in the database
        student_database[student_id]['First Name'] = Fname
        student_database[student_id]['Last Name'] = Lname
        student_database[student_id]['Year'] = Year
        student_database[student_id]['Department'] = Department
        print(f"Student with ID {student_id}'s information updated successfully!\n")
    else:
        print(f"Student with ID {student_id} not found in the database.\n")

def delete_student():
    student_id = input("Enter student ID to delete: ").upper()
    if student_id in student_database:
        # Delete the student from the database
        del student_database[student_id]
        print(f"Student with ID {student_id} deleted from the database.\n")
    else:
        print(f"Student with ID {student_id} not found in the database.\n")

# Main program loop
while True:
    print("Student Database Program")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_all_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
