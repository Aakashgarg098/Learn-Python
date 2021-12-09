class Programmer:
    language = "Python"
    _role = "Data Scientist"
    __salary = 10000000

p1 = Programmer()
print(p1.language,p1._role,p1._Programmer__salary)

class Aakash(Programmer):
    pass
aakash = Aakash()
print(aakash.language,aakash._role,aakash._Programmer__salary)
