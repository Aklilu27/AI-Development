def register_student():
    name = input("Enter full name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    with open("students.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone: {phone}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Course: {course}\n")
        file.write("-" * 30 + "\n")

    print("✅ Student registered successfully!\n")


def view_students():
    print("\n=== Registered Students ===\n")
    try:
        with open("students.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("⚠ No records found.\n")


# Main menu loop
while True:
    print("1. Register Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye !")
        break
    else:
        print("Invalid choice, try again.\n")
