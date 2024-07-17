from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    class_room: str

s1 = Student('John', 12, 'JSS!')
s2 = Student('Kunle', 16, 'JSS3')

if s1.name == 'John':
    print(s1.name)
else:
    print("Please ask the class teacher")
