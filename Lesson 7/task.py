"""break, continue, pass"""


index = 1

while index <= 5:
    number = int(input("Enter number: "))

    if number < 0:
        print("Negative number")
        continue

    if  number == 999:
        print("STOP ")
        break

    print(number * 2)
    index += 1

