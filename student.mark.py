students = []
courses = []
marks = {}

# Input number of students
def input_studentNumber():
    try:
        return int(input("Number of students: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return input_studentNumber()

# Input student information
def input_student_information():
    num_students = input_studentNumber()
    for _ in range(num_students):
        studentID = input("Enter student ID: ")
        studentName = input("Enter student name: ")
        studentDOB = input("Enter student DOB (dd/mm/yyyy): ")

        student = {
            "ID": studentID,
            "Name": studentName,
            "Dob": studentDOB
        }
        students.append(student)

# Input number of courses
def input_courseNumber():
    try:
        return int(input("Number of courses: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return input_courseNumber()

# Input course information
def input_course_information():
    num_courses = input_courseNumber()
    for _ in range(num_courses):
        courseID = input("Enter course ID: ")
        courseName = input("Enter course name: ")
        course = {
            "ID": courseID,
            "Name": courseName
        }
        courses.append(course)

# Input marks for a course
def input_mark():
    id_course = input("Enter the course ID to input marks: ")
    course_exists = any(course["ID"] == id_course for course in courses)
    if not course_exists:
        print("Course not found!")
        return

    marks[id_course] = {}
    for student in students:
        try:
            mark = float(input(f"Enter mark for student {student['Name']} (ID: {student['ID']}): "))
            marks[id_course][student["ID"]] = mark
        except ValueError:
            print("Invalid mark! Please enter a number.")
            return input_mark()

# List of students
def list_student():
    if not students:
        print("No students available.")
        return
    for student in students:
        print(f"Student ID: {student['ID']}, Name: {student['Name']}, DOB: {student['Dob']}")

# List of courses
def list_course():
    if not courses:
        print("No courses available.")
        return
    for course in courses:
        print(f"Course ID: {course['ID']}, Name: {course['Name']}")

# Show marks for a course
def show_mark():
    id_course = input("Enter the course ID to show marks: ")
    if id_course not in marks:
        print("Marks not found for this course!")
        return

    print(f"Marks for course {id_course}:")
    for student in students:
        id_student = student["ID"]
        if id_student in marks[id_course]:
            print(f"Student {student['Name']} (ID: {id_student}): {marks[id_course][id_student]}")
        else:
            print(f"Student {student['Name']} (ID: {id_student}): No mark available")

# Menu
def menu():
    while True:
        print("\n****** MENU ******")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List of all students")
        print("5. List of all courses")
        print("6. Show marks for a course")
        print("7. EXIT")

        try:
            user_choice = int(input("Enter your choice (1-7): "))
            if user_choice == 1:
                input_student_information()
            elif user_choice == 2:
                input_course_information()
            elif user_choice == 3:
                input_mark()
            elif user_choice == 4:
                list_student()
            elif user_choice == 5:
                list_course()
            elif user_choice == 6:
                show_mark()
            elif user_choice == 7:
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

# Run the program
menu()
