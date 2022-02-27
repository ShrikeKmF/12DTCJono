class Student:
    def __init__(self, name, age, phone_number, form_class, subjects,
                 gender):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = []
        self.gender = True
        self.enrolled = True
        student_list.append(self)

    def student_details(self):
        print(self.name)
        print(self.age)
        print(self.phone_number)
        print(self.form_class)
        print(self.subjects)
        print(self.gender)
        print(self.enrolled)
        print("###############################")


def print_student_info():
    for book in student_list:
        book.book_details()


def select_student_age():
    ageNum = 0
    student_age = input("Enter the age of the student: ")
    for student in student_list:
        while ageNum != count(student_list):
            if student.age >= student_age:
                print(f"This student {student.name} is over the age of 17")
                return student
                ageNum += 1
    print("Sorry no student with that age range has been found")
    return None


student_list = []

# Students Testing List
Student("Karen", "17", "123-4567", "WNLR", "13DTC, 13SMX", False)
Student("Bob", "18", "021-0263674", "BNNL", "13SMX", True)
Student("Lisa", "16", "022-4567123", "SKWR", "13DTC, 13SMX", False)
Student("Patrick", "18", " 023-01234567", "SCBE", "13ENG, 13CMX, 135MX, "
                                                   "13DTC", True)

select_student_age()
