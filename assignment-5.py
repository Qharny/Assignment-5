# Assignment 1

class Person:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

class Student(Person):
    def __init__(self, name, age, role, level, programme):
        super().__init__(name, age, role)
        self.level = level
        self.programme = programme


    def change_programme(self, new_programme):
        self.programme = new_programme


    def display_details(self):
        return f"{self.name} is {self.age} and is a {self.role}. \n {self.name} is in level {self.level} and offers {self.programme}"



class Lecturer(Person):
    def __init__(self, name, age, role, department):
        super().__init__(name, age, role)
        self.department = department
        self.courses = []


    def add_course(self, course):
        self.courses.append(course)


    def remove_course(self, course):
        self.courses.remove(course)


    def display_details(self):
            if len(self.courses) == 0:
                course_info = f"{self.name} is not assigned any course yet."
            else:
                course_info = f"{self.name} teaches {self.courses}"
                return f"{self.name} is {self.age} and is a {self.role}. \n {course_info}"
            

student1 = Student("John Doe", 20, "Student", 200, "Computer Science")
lecturer1 = Lecturer("Dr. Smith", 45, "Professor", "Computer Science Department")
lecturer1.add_course("Computer Architecture")
lecturer1.add_course("Data Structures")

print(student1.display_details())
print(lecturer1.display_details())




