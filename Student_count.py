# Counting the number of students in a class:

class Student:
    count = 0
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        Student.count += 1
    def display(self):
        print(self.name)
        print(self.phone)

st1 = Student(name = "Spandan" , phone = 99999)
st2 = Student(name = "Navya" ,phone = 88888)
st3 = Student(name = "Divyansh" , phone = 77777)
print("The number of students are: ",Student.count)
