# Python built-in class functions:
class Student:
    name = None
    identity = None
    age = None
    phone = None
    def __init__(self,name,identity,age,phone):
        self.name = name
        self.identity = identity
        self.age = age
        self.phone = phone
st = Student(name = "Spandan" , identity = 101 , age = 21 , phone = 99999)
print(getattr(st,'name'))   #getattr(object_name,attribute_name)
print(setattr(st,"section",'S'))  #setattr(object_name,attribute_name,attribute_value)
print(hasattr(st,"name"))    #hasattr(object_name,attribute_name)
print(delattr(st,"section")) #delattr(object_name,attribute_name)
