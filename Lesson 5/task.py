"""comparison operator: if, elif, else"""

age = int(input("Enter your age: "))

if 0 < age <= 6:
    print("Siz go'daksiz 😄")

elif 7 <= age <= 18:
    print("Siz o'quvchisiz 🏫")

elif 19 <= age <= 25:
    print("Siz talabasiz 🎓")

elif 26 <= age <= 60:
    print("Siz ishchisiz 👨‍💼")

else:
    print("Siz nafaqadasiz 👴")