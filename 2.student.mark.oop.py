class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.student_name}, DOB: {self.student_dob}"

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}"

class MarksManager:
    def __init__(self):
        self.marks = {}

    def input_marks(self, course_id, students):
        if course_id not in self.marks:
            self.marks[course_id] = {}

        for student in students:
            try:
                mark = float(input(f"Enter mark for student {student.student_name} (ID: {student.student_id}): "))
                self.marks[course_id][student.student_id] = mark
            except ValueError:
                print("Invalid mark! Please enter a number.")

    def show_marks(self, course_id, students):
        if course_id not in self.marks:
            print("Marks not found for this course!")
            return

        print(f"Marks for course {course_id}:")
        for student in students:
            if student.student_id in self.marks[course_id]:
                print(f"Student {student.student_name} (ID: {student.student_id}): {self.marks[course_id][student.student_id]}")
            else:
                print(f"Student {student.student_name} (ID: {student.student_id}): No mark available")

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks_manager = MarksManager()

    def input_student_information(self):
        num_students = self._get_number_input("Number of students: ")
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student DOB (dd/mm/yyyy): ")
            student = Student(student_id, student_name, student_dob)
            self.students.append(student)

    def input_course_information(self):
        num_courses = self._get_number_input("Number of courses: ")
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_marks(self):
        course_id = input("Enter the course ID to input marks: ")
        course_exists = any(course.course_id == course_id for course in self.courses)
        if not course_exists:
            print("Course not found!")
            return
        self.marks_manager.input_marks(course_id, self.students)

    def list_students(self):
        if not self.students:
            print("No students available.")
            return
        for student in self.students:
            print(student)

    def list_courses(self):
        if not self.courses:
            print("No courses available.")
            return
        for course in self.courses:
            print(course)

    def show_marks(self):
        course_id = input("Enter the course ID to show marks: ")
        self.marks_manager.show_marks(course_id, self.students)

    def _get_number_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter an integer.")

    def menu(self):
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
                    self.input_student_information()
                elif user_choice == 2:
                    self.input_course_information()
                elif user_choice == 3:
                    self.input_marks()
                elif user_choice == 4:
                    self.list_students()
                elif user_choice == 5:
                    self.list_courses()
                elif user_choice == 6:
                    self.show_marks()
                elif user_choice == 7:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice! Please select a number between 1 and 7.")
            except ValueError:
                print("Invalid input! Please enter an integer.")

# Running the program
if __name__ == "__main__":
    school = School()
    school.menu()
