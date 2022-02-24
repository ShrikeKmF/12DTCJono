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

    def student_details(self):
        print(self.name)
        print(self.age)
        print(self.phone_number)
        print(self.form_class)
        print(self.subjects)
        print(self.gender)
        print(self.enrolled)
        print("###############################")


# Students Testing List
Student("Bob", "18", "021-0263674", "BNNL", " 13SMX", True)
Student("Lisa", "16", "022-4567123", "SKWR", " 13DTC,13SMX", False)
Student("Patrick", "18", " 023-01234567", " SCBE", " 13ENG, 13CMX, 135MX, "
                                                   "13DTC", True)
Student("Karen", "17", "123-4567", "WNLR", "13DTC,13SMX", True)
