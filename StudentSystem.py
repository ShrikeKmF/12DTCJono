class Student:
    def __init__(self, name, age, phone_number, form_class, subjects,
                 gender):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = gender
        self.enrolled = True
        student_list.append(self)

    def student_details(self):
        print(f"\nName: {self.name}")
        print("###############################")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone_number}")
        print(f"Form Class: {self.form_class}")
        print(f"Subjects: {self.subjects}")
        if self.is_male:
            print("Gender: Male")
        elif not self.is_male:
            print("Gender: Female")
        else:
            print(self.is_male)
        print(f"Enrolled: {self.enrolled}")
        print("###############################\n")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        teacher_list.append(self)

    def teacher_details(self):
        print("--Teacher--")
        print(f"\nName: {self.name}")
        print(f"Subject: {self.subject}")
        print("###############################\n")


def print_student_info():
    for student in student_list:
        Student.student_details(student)


def print_teacher_info():
    for teacher in teacher_list:
        Teacher.teacher_details(teacher)


def select_student_age():
    student_age = int(input("Enter the age of the student: "))
    for student in student_list:
        if student.age >= student_age:
            Student.student_details(student)


def generate_students():
    # available form classes are: "BAKER", "MORGAN", "MCNICOL", "GRAHAM", "BELL", "NIMMO", "BARKER"
    # available classes are: "ART", "ENG", "MAT", "GRA", "DTC", "PHY", "BIO"
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)


def count_students(listCount):
    studentClass = input("What Subject are you looking for: ").upper()
    for student in student_list:
        if studentClass in student.subjects:
            listCount += 1
    print(f"There are '{listCount}' students in that class")


def find_student():
    student_to_find = input("Enter the name of the user: ").title()
    for student in student_list:
        if student.name in student_to_find:
            student.student_details()
            return student
    print("Sorry no student with that name has been found")
    return None


def add_student():
    name = input("Enter a new Students name: ").title()
    age = int(input("Enter Students Age: "))
    phone_number = input("Enter Students Number: ")
    form_class = input("Enter Students Form Class: ").upper()
    subjects = input("Enter Students Subjects (Separated by ,): ").upper()
    is_male = (input("Enter Students Gender (True=Male, False=Female): "))
    Student(name, age, phone_number, form_class, subjects, is_male)
    print(f"{name} Has been added to Student list")


def purge_student():
    student = find_student()
    print()
    if not student:
        print(f"Sorry, '{student.name}' is not on record")
    else:
        confirm = input("Type Y if you want to purge this student: "
                        "").upper()
        if confirm == "Y":
            print(f"Student Name: {student.name} is now purged")
            student_list.remove(student.name)


def menu():
    new_action = True
    while new_action:
        print("#############################")
        print("-----School System Menu-----")
        print("1. Student List")
        print("2. Students in Subject")
        print("3. Find Student")
        print("4. Students Above the Age of")
        print("5. Add new Student")
        print("6. Delete Student")
        print("7. Teacher List")
        print("8. Exit")
        print("#############################")
        choice = input("\nWhat would you like to do: ")
        if choice == "1":
            print_student_info()
        elif choice == "2":
            count_students(listCount)
        elif choice == "3":
            find_student()
        elif choice == "4":
            select_student_age()
        elif choice == "5":
            add_student()
        elif choice == "6":
            purge_student()
        elif choice == "7":
            print_teacher_info()
        elif choice == "8":
            new_action = False
        else:
            print("That is not a menu item please try again ")
    print("\n\nThank you for using the Student System")


listCount = 0
student_list = []
teacher_list = []

Teacher("Baker", "GRA")
Teacher("Barker", "MAT")
Teacher("Graham", "BIO")
Teacher("Morgan", "DTC")
Teacher("Bell", "PHY")
Teacher("Nimmo", "ART")
Teacher("McNicol", "ENG")

generate_students()
menu()
