"""function"""

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))


def calculator(number1: int,number2: int):
    yegindisi = number1 + number2
    print(yegindisi)
    ayirmasi = number1 - number2
    print(ayirmasi)
    kopaytmasi = number1 * number2
    print(kopaytmasi)
    if number2 != 0:
        bolinmasi = number1 / number2
        print(bolinmasi)
    else:
        print('0 ga bolinmaydi')
    print("Hisoblash yakunlandi")

calculator(num1,num2)