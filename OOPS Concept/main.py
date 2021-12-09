# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def print_result(self):
#         return self.name, self.age
# aakash = Student("Aakash", 23)
# harry = Student("Harry", 25)
# print(aakash.print_result())

# Instance Variable + Class Variable
# class Employee:
#     no_of_leaves = 8
# rohan = Employee()
# aakash = Employee()
# print(Employee.no_of_leaves)
# rohan.no_of_leaves = 10
# print(rohan.__dict__)
# print(Employee.no_of_leaves)

# Class Method
class Employee:
    no_of_leaves = 8

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        return f"{self.name} {self.age}"

    @classmethod
    def change(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, str):
        val = str.split("-")
        return cls(*val)

    @staticmethod
    def only_print():
        print("This is a static method")

rohan = Employee("Rohan", 26)
aakash = Employee("Aakash", 23)
harry = Employee.from_str("Harry-30")
print(harry.print_details())
print(aakash.print_details())
print(rohan.__dict__)
aakash.change(34)
print(rohan.no_of_leaves)
harry.only_print()