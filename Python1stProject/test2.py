class Person:
    def __init__(self, id, n):
        self.id = id
        self.name = n


class Student(Person):
    def __init__(self, id, n):
        super().__init__(id, n)

    def printDetails(self):
        print("Student:")
        print(self.id)
        print(self.name)


class Faculty(Person):
    def __init__(self, id, n):
        super().__init__(id, n)

    def printDetails(self):
        print("Faculty:")
        print(self.id)
        print(self.name)


class PhDStud(Student, Faculty):
    def __init__(self, id, n):
        super().__init__(id, n)


# Driver Code
ps = PhDStud(101, "Sandeep")
ps.printDetails()