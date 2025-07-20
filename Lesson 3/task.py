"""data type: int, float, str, bool"""

name =str(input("Entr your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
is_student = bool(input("Are you student: "))

print(f"name: {name} - {type(name)}")
print(f"age: {age} - {type(age)}")
print(f"height: {height} - {type(height)}")
print(f"Student: {is_student} - {type(is_student)}")