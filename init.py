class Student:
    collegeName="DD University"
    def __init__(self,name,course):
        print("Whenever a new object is created i am called automaticaly")
        print(self)
        self.name=name
        self.course=course
        print(self.name)
        print(self.course)
student1=Student("ANNIE","BCA")#init method will be called
print("Student1 Name",student1.name)
print("Student1 course",student1.course)
print(student1.collegeName)
student2=Student("MANI","PLASTIC ENGINEERING")
print("Student2 Name",student2.name)
print("Student2 course",student2.course)
print(student2)