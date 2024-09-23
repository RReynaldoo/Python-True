# Class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created  from that class

def main():
    student1 = Student("Louise",22)
    print(student1.name)
    print(Student.num_students)     #You can access this variable with objects but its good practice to do so with the name of the class



class Student:

    num_students = 0    #Class variable

    def __init__(self,name,age):
        self.name = name            #Object variable
        self.name = age
        Student.num_students += 1