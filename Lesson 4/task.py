"""Operators: (+, -, *, /, %, //, **, and, or, not)"""

number1 = float(input("Enter number: "))
number2 = float(input("Enter number: "))



addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
floor_division = number1 // number2
modulus = number1 % number2
exponentiation = number1 ** number2



print(f"""
addition: {addition}
subtraction: {subtraction}
multiplication: {multiplication}
division: {division}
floor_division: {floor_division}
modulus: {modulus}
exponentiation: {exponentiation}
""")