def student(**kwargs):
    student_name = kwargs.get('name', 'Unknown')
    student_age = kwargs.get('age', 'Unknown')
    print("Student Name:", student_name)
    print("Student Age:", student_age)
student(name="Alice", age=21)
