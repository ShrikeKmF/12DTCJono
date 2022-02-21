class AllStaff:
    staff = []

    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job

    def show(self):
        print(f"ID {self.id}, Name {self.name}, Age {self.age}, "
              f"Birthdate {self.birthdate}, "
              f"Role {self.job}")


class Management(AllStaff):
    def __init__(self, name, age, id, birthdate, job, car):
        super().__init__(name, age, id, birthdate, job)
        self.car = car

    def show(self):
        print(f"ID {self.id}, Name {self.name}, Age {self.age}, "
              f"Birthdate {self.birthdate}, "
              f"Role {self.job}, Drives {self.car}")


class Cleric(AllStaff):
    def __init__(self, name, age, id, birthdate, job, typing):
        super().__init__(name, age, id, birthdate, job)
        self.typing = typing

    def show(self):
        print(f"ID {self.id}, Name {self.name}, Age {self.age}, "
              f"Birthdate {self.birthdate}, "
              f"Role {self.job}, Types At {self.typing}WPM")


class Factory(AllStaff):
    def __init__(self, name, age, id, birthdate, job):
        super().__init__(name, age, id, birthdate, job)

    def show(self):
        print(f"ID {self.id}, Name {self.name}, Age {self.age}, "
              f"Birthdate {self.birthdate}, "
              f"Role {self.job}")


s1 = Management("Jim Charlston", "28", "01", "17/9/94", "Principal", "Audi R8")
s1.show()

c1 = Cleric("Jamie League", "16", "02", "17/9/04", "Admin", "80")
c1.show()

f1 = Factory("Sam Jacob", "22", "03", "12/12/00", "Mechanic")
f1.show()
