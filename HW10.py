# Base class for all people in the academy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Class for teachers, inherits from Person
class Teacher(Person):
    def __init__(self, name, age, subjects):
        super().__init__(name, age)
        self.subjects = subjects  # teachers have subjects they teach

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self):
        return f"Teacher: {super().__str__()}, Subjects: {', '.join(self.subjects)}"

# Class for students, inherits from Person
class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year  # year of study
        self.subjects = []  # list of subjects the student is enrolled in

    def enroll_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self):
        # Convert each subject in the list to its string representation
        subject_names = [str(subject) for subject in self.subjects]
        return f"Student: {super().__str__()}, Year: {self.year}, Subjects: {', '.join(subject_names)}"
# Class for subjects
class Subject:
    def __init__(self, name, teacher=None):
        self.name = name
        self.teacher = teacher  # teacher who leads the subject

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def __str__(self):
        return f"Subject: {self.name}, Teacher: {self.teacher.name if self.teacher else 'unassigned'}"

# Class for the academy
class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self):
        return (f"Academy: {self.name}\n" +
                f"Teachers: {', '.join(str(teacher) for teacher in self.teachers)}\n" +
                f"Students: {', '.join(str(student) for student in self.students)}\n" +
                f"Subjects: {', '.join(str(subject) for subject in self.subjects)}")

# Example of creating objects and working with them
academy = Academy("Kyiv Polytechnic")

# Creating subjects
math = Subject("Mathematics")
physics = Subject("Physics")

# Adding subjects to the academy
academy.add_subject(math)
academy.add_subject(physics)

# Creating teachers
teacher_anna = Teacher("Anna", 34, ["Physics"])
teacher_oleg = Teacher("Oleg", 45, ["Mathematics"])

# Assigning teachers to subjects
math.assign_teacher(teacher_oleg)
physics.assign_teacher(teacher_anna)

# Adding teachers to the academy
academy.add_teacher(teacher_anna)
academy.add_teacher(teacher_oleg)

# Creating students
student_john = Student("John", 20, 2)
student_lisa = Student("Lisa", 19, 1)

# Enrolling students in subjects
student_john.enroll_subject(math)
student_lisa.enroll_subject(physics)

# Adding students to the academy
academy.add_student(student_john)
academy.add_student(student_lisa)

# Display information about the academy
print(academy)
