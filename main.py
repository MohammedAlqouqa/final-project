
class Course:
    id_counter = 0

    def __init__(self, name, level):
        Course.id_counter += 1
        self.course_id = Course.id_counter
        self.course_name = name
        self.course_level = level

class Student:
    id_counter = 0

    def __init__(self, name, level):
        Student.id_counter += 1
        self.student_id = Student.id_counter
        self.student_name = name
        self.student_level = level
        self.student_courses = []

    def add_course(self, course):
        if course.course_level == self.student_level:
            self.student_courses.append(course)
            print("Course added successfully")
        else:
            print("Course level does not match student level")

    def display_details(self):
        print("Name:", self.student_name)
        print("Level:", self.student_level)
        print("Courses enrolled:")
        for course in self.student_courses:
            print(course.course_name, "-", course.course_level)

courses = []
students = []

while True:
    # Student Course Management System Menu
    # 1. Add new student
    # 2. Remove student
    # 3. Edit student
    # 4. Display all students
    # 5. Create new course
    # 6. Add course to student
    # 7. Exit

    choice = int(input("Enter choice (1-7): "))

    if choice == 1:
        name = input("Enter student name: ")
        level = input("Enter student level (A/B/C): ")
        while level not in ["A", "B", "C"]:
            level = input("Invalid input. Please enter student level again (A/B/C): ")
        student = Student(name, level)
        students.append(student)
        print("Student saved successfully")

    elif choice == 2:
        id = int(input("Enter student ID: "))
        found = False
        for student in students:
            if student.student_id == id:
                students.remove(student)
                found = True
                print("Delete done successfully")
                break
        if not found:
            print("User does not exist")

    elif choice == 3:
        id = int(input("Enter student ID: "))
        found = False
        for student in students:
            if student.student_id == id:
                new_name = input("Enter new name: ")
                new_level = input("Enter new level (A/B/C): ")
                while new_level not in ["A", "B", "C"]:
                    new_level = input("Invalid input. Please enter student level again (A/B/C): ")
                student.student_name = new_name
                student.student_level = new_level
                found = True
                print("Student updated successfully")
                break
        if not found:
            print("User does not exist")

    elif choice == 4:
        print("All students:")
        for student in students:
            student.display_details()

    elif choice == 5:
        name = input("Enter course name: ")
        level = input("Enter course level (A/B/C): ")
        while level not in ["A", "B", "C"]:
            level = input("Invalid input. Please enter course level again (A/B/C): ")
        course = Course(name, level)
        courses.append(course)
        print("Course created successfully")

    elif choice == 6:
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        student_found = False

    elif choice == 7:
        break




























