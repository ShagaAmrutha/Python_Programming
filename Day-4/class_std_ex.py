class Student:
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}")
std1 = Student()
std1.name = "Alice"
std1.rollno = 23
std1.marks = 95

std2 = Student()
std2.name = "Bob"
std2.rollno = 45
std2.marks = 88

std1.display()
std2.display()
