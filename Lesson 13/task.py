"""try except"""


try:
    son = int(input("Sun: "))
    son2 = int(input("Sun: "))
    result = son / son2
    print(result)
except ZeroDivisionError as e:
    print(e)