# coding upfront with python

x = "helo"
print(type(x))  # Output: <class 'int'>

def hello():
    print("hello")

print(type(hello))

# inbuild methods in python forexample

name = "Okello peter"
print(name.upper())

#dealing with classes in python 

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def display_marks(self):
        print(f"My marks are {self.marks}.")

st1 = Student("Okello", 20, 85)
st1.greet()  # Output: Hello, my name is Okello and I am
