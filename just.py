import re

email = input("What's your email address?").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("invalid")


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student
