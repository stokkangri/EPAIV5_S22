class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"

class Student(Person):
    def __init__(self, name, age, job, grade):
        super().__init__(name, age, job)
        self.grade = grade
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Grade: {self.grade}"

class Professor(Person):
    def __init__(self, name, age, job, courses):
        super().__init__(name, age, job)
        self.courses = courses
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Courses: {self.courses}"

class Employee(Person):
    def __init__(self, name, age, job, department):
        super().__init__(name, age, job)
        self.department = department
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Department: {self.department}"

class StudentProfessor(Student, Professor):
    def __init__(self, name, age, job, courses, grade):
        Person.__init__(self, name, age, job)
        self.grade = grade
        self.courses = courses
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Courses: {self.courses}, Grade: {self.grade}"

class Location:
    __slots__ = ['name', 'longitude', 'latitude']
    
    def __init__(self, name, longitude, latitude):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
    
    def get_coordinates(self):
        return (self.longitude, self.latitude)