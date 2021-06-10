# Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class. Create a function to display the entire attribute and their values in Student class
class Student:
    student_id = 'V10'
    student_name = 'Jacqueline Barnett'
    def display():
        print(f'Student id: {Student.student_id}\nStudent Name: {Student.student_name}')
print("Original attributes and their values of the Student class:")
Student.display()