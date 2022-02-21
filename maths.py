
# Student Class
class Student:
    def __int__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # int 0-100

    def get_grade(self):
        return self.grade


class Course:
    def __int__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
            return total / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("jill", 19, 65)

course1 = Course("Computer Science", 2)

course1.add_student(s1)
course1.add_student(s2)

for student in course1.students:
    print(student.name)

print(f"The average grade in {course1.name} is {course1.get_average_grade()}")
