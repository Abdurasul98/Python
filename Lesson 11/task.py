"""*args **kwargs"""
# ------------------------------------------------------------

# def my_sum(*args):
#     summa = 0
#     for i in args:
#         summa += i
#     print(summa)
#     return summa
# number1 = int(input("Number: "))
# number2 = int(input("Number: "))
# number3 = int(input("Number: "))
# number4 = int(input("Number: "))
#
# my_sum(number1,number2,number3,number4)

# ------------------------------------------------------------
ism = input("ism: ")
yosh = int(input("yosh: "))
shahar = input("shahar: ")

def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"natija:{key} = {value}")
print_info(ism=ism,yosh=yosh,shahar=shahar)