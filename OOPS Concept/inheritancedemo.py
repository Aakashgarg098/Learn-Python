# Single Inheritance
# class Employee:
#     no_of_leaves = 10
#     def __init__(self, aname, aage, asalary):
#         self.name = aname
#         self.age = aage
#         self.salary = asalary
#     def print_details(self):
#         return f"{self.name} {self.age} {self.salary}"
#     @classmethod
#     def change_leaves(cls, leaves):
#         cls.no_of_leaves = leaves
#     @classmethod
#     def conso(cls, string):
#         return cls(*string.split("-"))
# aakash = Employee("Aakash", 23, 100000000)
# rohan = Employee("Rohan", 25, 10000)
# harry = Employee.conso("Harry-33-100000")
# print(aakash.print_details(),aakash.no_of_leaves)
# aakash.change_leaves(20)
# print(harry.print_details(),harry.no_of_leaves)

# class Programmer(Employee):

    # def print_details(self):
    #     return f"{self.name} {self.age}"
# aakash = Programmer("Aakash", 23, 100000000)
# rohan = Programmer("Rohan", 25, 10000)
print(aakash.print_details())

# Multiple Inheritance
# class Employee:
#     no_of_leaves = 10
#     def __init__(self, aname, aage, asalary):
#         self.name = aname
#         self.age = aage
#         self.salary = asalary
#     def print_details(self):
#         return f"{self.name} {self.age} {self.salary}"
#     @classmethod
#     def change_leaves(cls, leaves):
#         cls.no_of_leaves = leaves
#     @classmethod
#     def conso(cls, string):
#         return cls(*string.split("-"))

# class Programmer:
#     def __init__(self, aname, aage, asalary, role):
#         self.role = role
#     def print_details(self):
#         return f"{self.name} {self.age} {self.role}"

# class Minded(Employee, Programmer):
#     pass
# aakash = Minded("Aakash", 23, 100000000)
# rohan = Minded("Rohan", 25, 10000)
# print(rohan.print_details())

# Multi Level Inheritance
# class Dad:
#     businessman = 1
# class Son(Dad):
#     coder = 1
#     def print_d(self):
#         print(f"{self.coder}")
# class Grandson(Son):
#     pass
# aakash = Grandson()
# aakash.print_d()