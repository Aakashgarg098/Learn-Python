# print("Hello, World!")
# print("Welcome","Aakash",sep=" | ")
# print("Bye " * 5, sep="\t")

# Single Line Comment
'''
This is a syntax of multi line comment
'''

# Input + Type Casting + Escape Sequence Character
# n1 = input("Enter the number1:\n")
# n2 = input("Enter the number2:\n")
# sum = int(n1) + int(n2)
# print("The addition is:\n" + str(sum))

# String
# s = "Aakash is the best coder in the world..."
# print(s,type(s),s.upper(),s.lower(),s.find("is"),s.capitalize(),s.center(100, "-"),s.title(),s.endswith("world"),s.swapcase(),sep="\n")
# print(s[::-1])

# List
# li = [1,2,3,4.43,43.43,int,"Aakash", 60]
# for i in li:
#     if str(i).isnumeric() and int(i)>6:
#         print(i, sep=" ")

# l1 = [1,2,3,4,5]
# l2 = ["a","b","c","d","e"]
# print(*zip(l1,l2))

# Tuple
# t = (1, )
# print(t)

# Set
# s = set()
# s.add(1)
# s.add(2)
# s.add(43.3)
# s.add(3)
# s.add(1)
# print(s)

# Dictionary
# dic = {"Aakash":"Programmer", "Manish":"Businessman","Nakul":"Property Dealer"}
# for k, v in dic.items():
#     print(k,v,sep=" : ")

# If-Else
# li = [1,2,3,55]
# if 50 in li:
#     print("Yes, it's in the list")
# elif 1 in li:
#     print("Oh, Found it..")
# else:
#     print("Sorry...")

# Break and Continue
# i = 1
# while i<50:
#     if i<5:
#         i += 1
#         continue
#     print(i,end=" ")
#     if i == 25:
#         break
#     i+=1

# Functions
# def add(*li):
    # """This program add multiple values at a time"""
#     return sum(*li)
#
# inp = int(input("How many values you want to enter???\n"))
# li = []
# i = 1
# while i<=inp:
#     val = int(input(f"Enter the value {i}:\n"))
#     li.append(val)
#     i+=1
#
# res = add(li)
# print(res)
# print(add.__doc__)

# Exception Handling
# n = int(input("Enter a number:\n"))
# try:
#     res = 10/n
#     print(res)
# except Exception as e:
#     print(e,"Exception.")
# else:
#     print("This will only executed if there is no exception to handle...")
# finally:
#     print("This will always printed...")

# File Handling
# f = open("file.txt", "w")
# f.write("Hi, This is Aakash...\n")
# f.close()

# f = open("file.txt", "a")
# f.write("I'm one of the top programmers in the world...")
# f.close()

# File + With Keyword
# with open("file1.txt","w") as f:
#     f.write("Aakash is a good boy...")
#     f.seek(0)
#     print(f.tell())
#     f.seek(10)
#     print(f.tell())

